[app]

title = Trading Bot
package.name = tradingbot
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,json,txt
version = 0.1

requirements = python3,kivy==2.1.0,https://github.com/kivy-garden/xwebview/archive/master.zip,pyjnius,android,plyer,yfinance,numpy,requests

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png
orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.api = 30
android.minapi = 21
android.ndk = 25b
android.gradle_dependencies = 'androidx.core:core:1.6.0'
android.private_storage = False
android.services = bot_service:bot_service.py
android.permissions = INTERNET,WAKE_LOCK,FOREGROUND_SERVICE,ACCESS_NETWORK_STATE
android.manifest_extra = <application android:usesCleartextTraffic="true" />
android.foreground_service = True
android.service_auto_restart = True
android.notification_channel_id = tradingbot_channel
android.notification_channel_name = Trading Bot Service
android.notification_id = 1001
android.notification_title = Trading Bot
android.notification_text = Bot is running in background

android.accept_sdk_license = True

p4a.branch = master
p4a.bootstrap = sdl2
p4a.service = bot_service
p4a.main = main.py
