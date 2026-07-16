[app]
title = Hopwet Guide
package.name = hopwetapp
package.domain = org.skyblue
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,requests

orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 1
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
android.api = 33
android.minapi = 24
android.ndk_api = 24

[buildozer]
log_level = 2
warn_on_root = 0
