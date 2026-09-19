#!/usr/bin/env bash
set +e
API="$1"
gradle :app:connectedDebugAndroidTest --stacktrace
BASE_STATUS=$?
gradle :app:assembleDebug
BUILD_STATUS=$?
INSTALL_STATUS=1
URI_STATUS=1
if [ "$BUILD_STATUS" -eq 0 ]; then
  adb install -r app/build/outputs/apk/debug/app-debug.apk
  INSTALL_STATUS=$?
fi
if [ "$BASE_STATUS" -eq 0 ] && [ "$INSTALL_STATUS" -eq 0 ]; then
  gradle :consumer:connectedDebugAndroidTest --stacktrace
  URI_STATUS=$?
fi
adb logcat -d -s SAFESEP_EVIDENCE:I '*:S' > "../evidence-api-${API}.txt" || true
if [ "$BASE_STATUS" -ne 0 ] || [ "$BUILD_STATUS" -ne 0 ] || [ "$INSTALL_STATUS" -ne 0 ] || [ "$URI_STATUS" -ne 0 ]; then
  exit 1
fi
exit 0
