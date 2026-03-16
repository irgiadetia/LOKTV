# Tambahkan requests dan certifi
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius,requests,certifi

# Pastikan permissions lengkap
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED, READ_CONTACTS

# Penting: Services harus merujuk ke file service jika ingin tetap jalan di background
# Tapi untuk tahap awal ini, pastikan main.py dulu yang benar.
