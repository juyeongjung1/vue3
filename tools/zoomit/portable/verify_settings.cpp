// 実際の設定クラスを、プロセス専用の一時レジストリで検証する。
#include "pch.h"
#include "ZoomItSettings.h"

void Check(bool condition, const char* message)
{
    if (!condition) throw message;
}

int main()
{
    wchar_t testKey[128];
    swprintf_s(testKey, L"Software\\ZoomItMutedGreenTest-%lu-%llu", GetCurrentProcessId(), GetTickCount64());
    HKEY root = nullptr;
    DWORD disposition = 0;
    if (RegCreateKeyExW(HKEY_CURRENT_USER, testKey, 0, nullptr, 0, KEY_ALL_ACCESS, nullptr, &root, &disposition) != ERROR_SUCCESS) return 1;
    if (disposition != REG_CREATED_NEW_KEY) { RegCloseKey(root); return 1; }
    int result = 0;
    try {
        Check(RegOverridePredefKey(HKEY_CURRENT_USER, root) == ERROR_SUCCESS, "registry isolation failed");
        const wchar_t* legacyKey = L"Software\\Sysinternals\\ZoomIt";
        DWORD oldColor = RGB(0, 255, 0), oldHotkey = (HOTKEYF_CONTROL << 8) | '9';
        Check(RegSetKeyValueW(HKEY_CURRENT_USER, legacyKey, L"PenColor", REG_DWORD, &oldColor, sizeof(oldColor)) == ERROR_SUCCESS, "legacy color setup failed");
        Check(RegSetKeyValueW(HKEY_CURRENT_USER, legacyKey, L"DrawToggleKey", REG_DWORD, &oldHotkey, sizeof(oldHotkey)) == ERROR_SUCCESS, "legacy hotkey setup failed");

        ClassRegistry settings(SETTINGS_KEY);
        settings.ReadRegSettings(RegSettings);
        Check(g_PenColor == COLOR_RED, "legacy color was imported");
        Check(g_DrawToggleKey == ((HOTKEYF_CONTROL << 8) | '2'), "legacy hotkey was imported");

        g_PenColor = COLOR_GREEN;
        g_DrawToggleKey = (HOTKEYF_CONTROL << 8) | '8';
        settings.WriteRegSettings(RegSettings);
        g_PenColor = 0;
        g_DrawToggleKey = 0;
        settings.ReadRegSettings(RegSettings);
        Check(g_PenColor == RGB(107, 158, 120), "muted green was not restored");
        Check(g_DrawToggleKey == ((HOTKEYF_CONTROL << 8) | '8'), "dedicated hotkey was not restored");

        DWORD saved = 0, size = sizeof(saved);
        Check(RegGetValueW(HKEY_CURRENT_USER, legacyKey, L"PenColor", RRF_RT_REG_DWORD, nullptr, &saved, &size) == ERROR_SUCCESS && saved == oldColor, "legacy color was changed");
        size = sizeof(saved);
        Check(RegGetValueW(HKEY_CURRENT_USER, legacyKey, L"DrawToggleKey", RRF_RT_REG_DWORD, nullptr, &saved, &size) == ERROR_SUCCESS && saved == oldHotkey, "legacy hotkey was changed");
        Check(wcscmp(APPNAME, L"ZoomItMutedGreen") == 0, "autostart name is not isolated");
        puts("Settings isolation: legacy settings ignored and preserved; dedicated settings saved and restored.");
    } catch (const char* message) {
        fprintf(stderr, "%s\n", message);
        result = 1;
    }
    RegOverridePredefKey(HKEY_CURRENT_USER, nullptr);
    RegCloseKey(root);
    RegDeleteTreeW(HKEY_CURRENT_USER, testKey);
    return result;
}
