# Monorepo Release Manager Demo

Purpose
- This repository is a small monorepo used to validate integration goals for the Release Manager tool. https://github.com/moveaxlab/release-manager

Repository layout
- be/
  - auth/        — Go (Cobra) authentication service
  - order/       — Python (FastAPI) orders service
  - payment/     — Java (Spring Boot) payment service
- fe/
  - desktop/     — 2 Electron desktop clients (admin, manager)
  - web/         — React (Vite) web frontend
  - mobile/      — React Native mobile app (android / ios)

At the moment version changes in code are only supported in react, react-native, electron. 
Where each service keeps its version:
- mobile/android: `mobile/android/app/build.gradle` -> `versionCode` / `versionName`
- mobile/ios: `mobile/ios/Config.xcconfig` -> `APP_VERSION` / `APP_BUILD`
- fe/web: `fe/web/package.json` -> `version`
- fe/desktop (Electron): `fe/desktop/*/package.json` -> `version`

