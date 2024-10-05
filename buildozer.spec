[app]

title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3, kivy
android.permissions = INTERNET
android.api = 29
android.arch = armeabi-v7a, arm64-v8a
#icon.filename = %(source.dir)s/icon.png
#source.include_patterns = assets/*
orientation = portrait
debug = 1
version = 0.1
source.main = main.py

android.sdk_path =  /home/runner/android-sdk
