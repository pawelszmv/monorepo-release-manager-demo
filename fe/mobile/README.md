Minimal React Native app.

Install and run (requires native toolchains for Android/iOS):

  cd mobile
  npm install
  npx react-native run-android   # android device/emulator
  npx react-native run-ios       # macOS + Xcode

Android version is set in:
  android/app/build.gradle (versionName / versionCode)

iOS version is set in:
  ios/Config.xcconfig (APP_VERSION / APP_BUILD)