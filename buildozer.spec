[app]
title = Space Shooter
package.name = spaceshooter
package.domain = org.space
source.dir = .
source.include_exts = py,wav
version = 1.0
requirements = python3,kivy,pygame-ce==2.4.1
orientation = portrait
fullscreen = 1
android.api = 31
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
