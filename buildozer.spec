[app]

title = MyApp
package.name = myapp
package.domain = org.test
source.include_exts = py,png,jpg,kv,atlas
requirements = python3, kivy
orientation = all
android.permissions = INTERNET
android.api = 29
android.arch = armeabi-v7a, arm64-v8a
fullscreen = 1
#icon.filename = %(source.dir)s/icon.png
#source.include_patterns = assets/*
debug = 1
version = 0.1
source.main = main.py

android.sdk_path = /usr/lib/android-sdk
