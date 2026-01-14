# Monorepo Release Manager Demo

Purpose
- This repository is a small monorepo used to validate integration goals for the Release Manager tool. https://github.com/moveaxlab/release-manager

Repository layout
- be/
  - auth/        — Go (Cobra) authentication service [CHANGELOG.md](be/auth/CHANGELOG.md)  
  - order/       — Python (FastAPI) orders service [CHANGELOG.md](be/order/CHANGELOG.md)
  - payment/     — Java (Spring Boot) payment service [CHANGELOG.md](be/payment/CHANGELOG.md)
- fe/
  - desktop/     — 2 Electron desktop clients
    - admin-client [CHANGELOG.md](fe/desktop/admin-client/CHANGELOG.md)
    - manager-client [CHANGELOG.md](fe/desktop/manager-client/CHANGELOG.md)
  - web/         — React (Vite) web frontend [CHANGELOG.md](fe/web/CHANGELOG.md)
  - mobile/      — React Native mobile app [CHANGELOG.md](fe/mobile/CHANGELOG.md)

The Release Manager will update the changelog for each of the projects in the monorepo, additionally it can also update the app version for some project types.

At the moment version changes in code are supported for react, react-native, electron. 
Where each service sets its version:
- mobile/android: `mobile/android/app/build.gradle` -> `versionCode` / `versionName`
- mobile/ios: `mobile/ios/Config.xcconfig` -> `APP_VERSION` / `APP_BUILD`
- fe/web: `fe/web/package.json` -> `version`
- fe/desktop (Electron): `fe/desktop/*/package.json` -> `version`
