[app]

# (str) Title of your application
title = Trading Bot

# (str) Package name
package.name = tradingbot

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source directory where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,json,txt

# (list) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivy_garden.xwebview,plyer,pyjnius,yfinance,pandas,numpy,requests

# (str) Presplash of the application
presplash.filename = %(source.dir)s/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (int) Android API to use
android.api = 30

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (str) Android SDK version to use
android.sdk = 30

# (list) Gradle dependencies
android.gradle_dependencies = 'androidx.core:core:1.6.0'

# (bool) Use Android private storage (True) or SD card (False)
android.private_storage = False

# (list) Android services (name:entrypoint)
android.services = bot_service:bot_service.py

# (list) Android permissions
android.permissions = INTERNET,WAKE_LOCK,FOREGROUND_SERVICE,ACCESS_NETWORK_STATE

# (str) python-for-android branch to use
p4a.branch = master

# (str) Service which will be started automatically
p4a.service = bot_service

# (str) The source directory of the main python file
p4a.source_dir = .

# (list) List of Java classes to be added to the APK
# android.add_src =

# (list) List of Java .jar files to add
# android.add_jars =

# (list) List of patterns for files to exclude from APK
# android.exclude_src =

# (str) Bootstrap to use (sdl2, webview, service_only)
# p4a.bootstrap = sdl2

# (list) Application meta-data
# android.meta_data = 

# (list) Additional Java classes to be added to the android project
# android.add_java = 

# (list) Patterns of files to exclude from the final APK
# android.exclude_patterns =

# (list) Additional arguments for the AndroidManifest.xml
# android.manifest_extra =

# (list) Additional arguments for ant
# android.ant_extra =

# (str) The Android logcat filter
# android.logcat_filters = *:S python:D

# (bool) Copy libraries instead of making big libs
# android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.arch = armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# android.numeric_version = 1

# (bool) If True, then skip trying to update the Android sdk
# android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
# android.accept_sdk_license = False

# (str) Android entry point to use
# android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
# android.whitelist =

# (str) Path to a custom AndroidManifest.xml file
# android.manifest = 

# (str) Path to a custom activity
# android.activity = 

# (str) Path to a custom service
# android.service = 

# (str) Path to a custom broadcast receiver
# android.broadcast_receiver = 

# (str) Path to a custom content provider
# android.content_provider = 

# (list) List of Java classes to add as activities
# android.add_activity = 

# (list) List of Java classes to add as services
# android.add_service = 

# (list) List of Java classes to add as broadcast receivers
# android.add_receiver = 

# (list) List of Java classes to add as content providers
# android.add_provider = 

# (str) The Java package for the generated R class
# android.r_package = 

# (str) The Java package for the generated BuildConfig class
# android.build_config_package = 

# (bool) If True, then compile in release mode
# android.release = False

# (str) The key alias to use for signing the release APK
# android.keyalias = 

# (str) The password for the key alias
# android.keypass = 

# (str) The keystore filename
# android.keystore = 

# (str) The password for the keystore
# android.storepass = 

# (str) The entry point for the Python service
# android.service_entrypoint = 

# (list) Arguments to be passed to the service
# android.service_args = 

# (bool) If True, the service will be started automatically
# android.start_service = True

# (bool) If True, the service will run in the foreground
# android.foreground_service = True

# (str) Notification channel id for foreground service
# android.notification_channel_id = 

# (str) Notification channel name for foreground service
# android.notification_channel_name = 

# (int) Notification id for foreground service
# android.notification_id = 

# (str) Notification title for foreground service
# android.notification_title = 

# (str) Notification text for foreground service
# android.notification_text = 

# (bool) If True, the service will be restarted automatically
# android.service_auto_restart = True

# (list) List of requirements to be added to the Python environment
# android.add_requirements = 

# (list) List of files/directories to be added to the assets
# android.add_assets = 

# (list) List of files/directories to be added to the res directory
# android.add_res = 

# (list) List of files/directories to be added to the libs directory
# android.add_libs = 

# (list) List of files/directories to be added to the src directory
# android.add_src = 

# (list) List of files/directories to be added to the jni directory
# android.add_jni = 

# (list) List of files/directories to be added to the assets/www directory
# android.add_www = 

# (str) Path to a custom build.gradle file
# android.build_gradle = 

# (str) Path to a custom settings.gradle file
# android.settings_gradle = 

# (str) Path to a custom gradle.properties file
# android.gradle_properties = 

# (list) List of Java classes to be added to the DEX classpath
# android.add_dex = 

# (list) List of Java classes to be added to the DEX classpath (for multidex)
# android.add_dex_multidex = 

# (bool) If True, then enable multidex
# android.enable_multidex = False

# (list) List of Java classes to be added to the DEX classpath (for multidex)
# android.multidex_keep = 

# (list) List of Java classes to be added to the DEX classpath (for multidex)
# android.multidex_keep_file = 

# (bool) If True, then enable proguard
# android.enable_proguard = False

# (str) Path to a custom proguard-rules.pro file
# android.proguard_rules = 

# (bool) If True, then enable jni debugging
# android.enable_jni_debugging = False

# (bool) If True, then enable Android App Bundle
# android.enable_aab = False

# (str) The version of the Android Gradle Plugin
# android.gradle_plugin_version = '3.4.0'

# (str) The version of Gradle
# android.gradle_version = '5.1.1'

# (str) The version of the Android SDK Build Tools
# android.build_tools_version = '28.0.3'

# (str) The version of the Android SDK Platform
# android.platform_version = '28'

# (bool) If True, then use the legacy packaging method
# android.legacy = False

# (bool) If True, then use the new packaging method
# android.new_packaging = True

# (bool) If True, then use the old toolchain
# android.old_toolchain = False

# (str) Path to a custom toolchain.py file
# android.toolchain = 

# (bool) If True, then enable NDK debugging
# android.enable_ndk_debugging = False

# (str) The NDK API to use
# android.ndk_api = 21

# (bool) If True, then use the C++ STL
# android.use_cxx_stl = False

# (str) The C++ STL to use
# android.cxx_stl = 'gnustl_static'

# (bool) If True, then use the C++ exceptions
# android.use_cxx_exceptions = False

# (bool) If True, then use the C++ RTTI
# android.use_cxx_rtti = False

# (list) List of environment variables to set
# android.env = 

# (list) List of additional Java options
# android.add_java_options = 

# (list) List of additional JNI options
# android.add_jni_options = 

# (list) List of additional C flags
# android.add_cflags = 

# (list) List of additional C++ flags
# android.add_cxxflags = 

# (list) List of additional linker flags
# android.add_ldflags = 

# (list) List of additional libraries
# android.add_libraries = 

# (list) List of additional static libraries
# android.add_static_libraries = 

# (list) List of additional shared libraries
# android.add_shared_libraries = 

# (list) List of additional include directories
# android.add_include_dirs = 

# (list) List of additional library directories
# android.add_library_dirs = 

# (list) List of additional assets directories
# android.add_assets_dirs = 

# (list) List of additional resource directories
# android.add_resource_dirs = 

# (list) List of additional Java source directories
# android.add_java_src_dirs = 

# (list) List of additional Java resource directories
# android.add_java_res_dirs = 

# (list) List of additional aidl directories
# android.add_aidl_dirs = 

# (list) List of additional renderscript directories
# android.add_renderscript_dirs = 

# (list) List of additional JNI directories
# android.add_jni_dirs = 

# (list) List of additional assets to be added to the APK
# android.add_assets_to_apk = 

# (list) List of additional resources to be added to the APK
# android.add_resources_to_apk = 

# (list) List of additional libraries to be added to the APK
# android.add_libraries_to_apk = 

# (list) List of additional shared libraries to be added to the APK
# android.add_shared_libraries_to_apk = 

# (list) List of additional files to be added to the APK
# android.add_files_to_apk = 

# (bool) If True, then include the Python source files in the APK
# android.include_python_source = False

# (bool) If True, then include the Python bytecode files in the APK
# android.include_python_bytecode = True

# (bool) If True, then use the old Python packaging
# android.old_python_packaging = False

# (bool) If True, then use the new Python packaging
# android.new_python_packaging = True

# (list) List of Python modules to exclude from the APK
# android.exclude_python_modules = 

# (list) List of Python modules to include in the APK
# android.include_python_modules = 

# (list) List of Python modules to freeze
# android.freeze_python_modules = 

# (bool) If True, then use the old SDL2 bootstrap
# android.old_sdl2_bootstrap = False

# (bool) If True, then use the new SDL2 bootstrap
# android.new_sdl2_bootstrap = True

# (str) The path to the SDL2 source directory
# android.sdl2_source_dir = 

# (str) The path to the SDL2 image source directory
# android.sdl2_image_source_dir = 

# (str) The path to the SDL2 mixer source directory
# android.sdl2_mixer_source_dir = 

# (str) The path to the SDL2 ttf source directory
# android.sdl2_ttf_source_dir = 

# (bool) If True, then use the old webview bootstrap
# android.old_webview_bootstrap = False

# (bool) If True, then use the new webview bootstrap
# android.new_webview_bootstrap = True

# (str) The path to the webview source directory
# android.webview_source_dir = 

# (bool) If True, then use the old service only bootstrap
# android.old_service_only_bootstrap = False

# (bool) If True, then use the new service only bootstrap
# android.new_service_only_bootstrap = True

# (str) The path to the service only source directory
# android.service_only_source_dir = 

# (bool) If True, then use the old pyjnius bootstrap
# android.old_pyjnius_bootstrap = False

# (bool) If True, then use the new pyjnius bootstrap
# android.new_pyjnius_bootstrap = True

# (str) The path to the pyjnius source directory
# android.pyjnius_source_dir = 

# (bool) If True, then use the old plyer bootstrap
# android.old_plyer_bootstrap = False

# (bool) If True, then use the new plyer bootstrap
# android.new_plyer_bootstrap = True

# (str) The path to the plyer source directory
# android.plyer_source_dir = 

# (bool) If True, then use the old kivy bootstrap
# android.old_kivy_bootstrap = False

# (bool) If True, then use the new kivy bootstrap
# android.new_kivy_bootstrap = True

# (str) The path to the kivy source directory
# android.kivy_source_dir = 

# (bool) If True, then use the old garden bootstrap
# android.old_garden_bootstrap = False

# (bool) If True, then use the new garden bootstrap
# android.new_garden_bootstrap = True

# (str) The path to the garden source directory
# android.garden_source_dir = 

# (bool) If True, then use the old xwebview bootstrap
# android.old_xwebview_bootstrap = False

# (bool) If True, then use the new xwebview bootstrap
# android.new_xwebview_bootstrap = True

# (str) The path to the xwebview source directory
# android.xwebview_source_dir = 

# (bool) If True, then use the old numpy bootstrap
# android.old_numpy_bootstrap = False

# (bool) If True, then use the new numpy bootstrap
# android.new_numpy_bootstrap = True

# (str) The path to the numpy source directory
# android.numpy_source_dir = 

# (bool) If True, then use the old pandas bootstrap
# android.old_pandas_bootstrap = False

# (bool) If True, then use the new pandas bootstrap
# android.new_pandas_bootstrap = True

# (str) The path to the pandas source directory
# android.pandas_source_dir = 

# (bool) If True, then use the old yfinance bootstrap
# android.old_yfinance_bootstrap = False

# (bool) If True, then use the new yfinance bootstrap
# android.new_yfinance_bootstrap = True

# (str) The path to the yfinance source directory
# android.yfinance_source_dir = 

# (bool) If True, then use the old requests bootstrap
# android.old_requests_bootstrap = False

# (bool) If True, then use the new requests bootstrap
# android.new_requests_bootstrap = True

# (str) The path to the requests source directory
# android.requests_source_dir = 

# (list) List of additional Java classes to be added to the APK
# android.add_java_classes = 

# (list) List of additional Java source files to be added to the APK
# android.add_java_sources = 

# (list) List of additional Java libraries to be added to the APK
# android.add_java_libraries = 

# (list) List of additional native libraries to be added to the APK
# android.add_native_libraries = 

# (list) List of additional assets to be added to the APK
# android.add_assets = 

# (list) List of additional resources to be added to the APK
# android.add_resources = 

# (list) List of additional files to be added to the APK
# android.add_files = 

# (bool) If True, then include the Python source files in the APK
# android.include_python_source = False

# (bool) If True, then include the Python bytecode files in the APK
# android.include_python_bytecode = True

# (bool) If True, then use the old Python packaging
# android.old_python_packaging = False

# (bool) If True, then use the new Python packaging
# android.new_python_packaging = True

# (list) List of Python modules to exclude from the APK
# android.exclude_python_modules = 

# (list) List of Python modules to include in the APK
# android.include_python_modules = 

# (list) List of Python modules to freeze
# android.freeze_python_modules = 

# (bool) If True, then use the old SDL2 bootstrap
# android.old_sdl2_bootstrap = False

# (bool) If True, then use the new SDL2 bootstrap
# android.new_sdl2_bootstrap = True

# (str) The path to the SDL2 source directory
# android.sdl2_source_dir = 

# (str) The path to the SDL2 image source directory
# android.sdl2_image_source_dir = 

# (str) The path to the SDL2 mixer source directory
# android.sdl2_mixer_source_dir = 

# (str) The path to the SDL2 ttf source directory
# android.sdl2_ttf_source_dir = 

# (bool) If True, then use the old webview bootstrap
# android.old_webview_bootstrap = False

# (bool) If True, then use the new webview bootstrap
# android.new_webview_bootstrap = True

# (str) The path to the webview source directory
# android.webview_source_dir = 

# (bool) If True, then use the old service only bootstrap
# android.old_service_only_bootstrap = False

# (bool) If True, then use the new service only bootstrap
# android.new_service_only_bootstrap = True

# (str) The path to the service only source directory
# android.service_only_source_dir = 

# (bool) If True, then use the old pyjnius bootstrap
# android.old_pyjnius_bootstrap = False

# (bool) If True, then use the new pyjnius bootstrap
# android.new_pyjnius_bootstrap = True

# (str) The path to the pyjnius source directory
# android.pyjnius_source_dir = 

# (bool) If True, then use the old plyer bootstrap
# android.old_plyer_bootstrap = False

# (bool) If True, then use the new plyer bootstrap
# android.new_plyer_bootstrap = True

# (str) The path to the plyer source directory
# android.plyer_source_dir = 

# (bool) If True, then use the old kivy bootstrap
# android.old_kivy_bootstrap = False

# (bool) If True, then use the new kivy bootstrap
# android.new_kivy_bootstrap = True

# (str) The path to the kivy source directory
# android.kivy_source_dir = 

# (bool) If True, then use the old garden bootstrap
# android.old_garden_bootstrap = False

# (bool) If True, then use the new garden bootstrap
# android.new_garden_bootstrap = True

# (str) The path to the garden source directory
# android.garden_source_dir = 

# (bool) If True, then use the old xwebview bootstrap
# android.old_xwebview_bootstrap = False

# (bool) If True, then use the new xwebview bootstrap
# android.new_xwebview_bootstrap = True

# (str) The path to the xwebview source directory
# android.xwebview_source_dir = 

# (bool) If True, then use the old numpy bootstrap
# android.old_numpy_bootstrap = False

# (bool) If True, then use the new numpy bootstrap
# android.new_numpy_bootstrap = True

# (str) The path to the numpy source directory
# android.numpy_source_dir = 

# (bool) If True, then use the old pandas bootstrap
# android.old_pandas_bootstrap = False

# (bool) If True, then use the new pandas bootstrap
# android.new_pandas_bootstrap = True

# (str) The path to the pandas source directory
# android.pandas_source_dir = 

# (bool) If True, then use the old yfinance bootstrap
# android.old_yfinance_bootstrap = False

# (bool) If True, then use the new yfinance bootstrap
# android.new_yfinance_bootstrap = True

# (str) The path to the yfinance source directory
# android.yfinance_source_dir = 

# (bool) If True, then use the old requests bootstrap
# android.old_requests_bootstrap = False

# (bool) If True, then use the new requests bootstrap
# android.new_requests_bootstrap = True

# (str) The path to the requests source directory
# android.requests_source_dir = 

# (list) List of additional Java classes to be added to the APK
# android.add_java_classes = 

# (list) List of additional Java source files to be added to the APK
# android.add_java_sources = 

# (list) List of additional Java libraries to be added to the APK
# android.add_java_libraries = 

# (list) List of additional native libraries to be added to the APK
# android.add_native_libraries = 

# (list) List of additional assets to be added to the APK
# android.add_assets = 

# (list) List of additional resources to be added to the APK
# android.add_resources = 

# (list) List of additional files to be added to the APK
# android.add_files = 

# (bool) If True, then include the Python source files in the APK
# android.include_python_source = False

# (bool) If True, then include the Python bytecode files in the APK
# android.include_python_bytecode = True

# (bool) If True, then use the old Python packaging
# android.old_python_packaging = False

# (bool) If True, then use the new Python packaging
# android.new_python_packaging = True

# (list) List of Python modules to exclude from the APK
# android.exclude_python_modules = 

# (list) List of Python modules to include in the APK
# android.include_python_modules = 

# (list) List of Python modules to freeze
# and
