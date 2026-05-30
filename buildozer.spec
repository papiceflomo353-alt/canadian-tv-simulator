[app]

# Basic app info
title = Canadian TV Simulator 2011
package.name = canadiantvSimulator
package.domain = org.canadiantv

# Source code location
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Requirements
requirements = python3,kivy

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Features
android.features = android.hardware.touchscreen

# App orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Icon and presplash
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]

# Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# Display warning on buildozer run
warn_on_root = 1

# Android SDK and NDK versions
android.api = 30
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Gradle options
android.gradle_dependencies =

# Java options
android.java_modules = org.kivy.android

# Default orientation
android.orientation = portrait

# Arch
android.archs = arm64-v8a,armeabi-v7a

# Bootstrap
p4a.bootstrap = sdl2

# Meta data
android.meta_data = com.google.android.gms.version=@integer/google_play_services_version
