"""MIT版ZoomItをソースからビルドして、配布用ZIPを作る。"""

import hashlib
import shutil
import subprocess
import sys
import time
import urllib.request
import zipfile
from pathlib import Path


UPSTREAM_COMMIT = "229a2894fa27c3a879132bd013f05951d4523660"
PACKAGES = {
    "Microsoft.Windows.CppWinRT": "2.0.240111.5",
    "Microsoft.Windows.ImplementationLibrary": "1.0.231216.1",
    "robmikh.common": "0.0.23-beta",
}


def run(*args, cwd=None):
    print("実行:", subprocess.list2cmdline([str(a) for a in args]), flush=True)
    subprocess.run([str(a) for a in args], cwd=cwd, check=True)


def replace_once(path, old, new):
    encoding = "cp1252" if path.suffix == ".rc" else "utf-8-sig"
    content = path.read_text(encoding=encoding)
    if content.count(old) != 1:
        raise RuntimeError(f"変更対象が一致しません: {path}")
    path.write_text(content.replace(old, new), encoding=encoding)


def main():
    upstream = Path(sys.argv[1]).resolve()
    work = Path(sys.argv[2]).resolve()
    actual = subprocess.check_output(
        ["git", "-C", str(upstream), "rev-parse", "HEAD"], text=True
    ).strip()
    if actual != UPSTREAM_COMMIT:
        raise RuntimeError("公開ソースのコミットが一致しません。")
    work.mkdir(exist_ok=False)
    source = work / "source"
    shutil.copytree(upstream / "src/modules/ZoomIt/ZoomIt", source)
    common = work / "common"
    shutil.copytree(upstream / "src/common/sysinternals", common, ignore=shutil.ignore_patterns("Eula"))
    package = work / "ZoomIt-MutedGreen-Windows-x64"
    package.mkdir()
    licenses = package / "licenses"
    licenses.mkdir()
    shutil.copy2(upstream / "LICENSE", package / "LICENSE.txt")

    replace_once(source / "ZoomIt.h", "RGB(0, 255, 0)", "RGB(107, 158, 120)")
    # MITの公開ソース版には、Sysinternals配布バイナリの利用契約を適用しない。
    replace_once(source / "Zoomit.cpp", "    if( !ShowEula( APPNAME, NULL, NULL )) return 1;", "    // MIT license and copyright notices are included with this build.")
    replace_once(source / "pch.h", '#include "Eula/eula.h"\n', "")
    for name in ("Zoomit.cpp", "ZoomIt.rc"):
        replace_once(source / name, "ZoomIt - Sysinternals: www.sysinternals.com", "ZoomIt - Muted Green (unofficial)")
    replace_once(source / "ZoomIt.rc", '"ZoomIt v9.0",IDC_VERSION,42,7,73,10', '"ZoomIt v9.0 - Muted Green",IDC_VERSION,42,7,220,10')

    # 単体版のバージョン情報。公式の配布元と誤認されないよう非公式版を明記する。
    (source / "version.h").write_text('''#pragma once
#define FILE_VERSION 9,0,0,1
#define PRODUCT_VERSION FILE_VERSION
#define FILE_VERSION_STRING "9.0.0.1"
#define PRODUCT_VERSION_STRING FILE_VERSION_STRING
#define COMPANY_NAME "Unofficial community build"
#define FILE_DESCRIPTION "ZoomIt Muted Green (unofficial)"
#define INTERNAL_NAME "ZoomIt-MutedGreen"
#define ORIGINAL_FILENAME "ZoomIt-MutedGreen.exe"
#define COPYRIGHT_NOTE "Copyright (C) Microsoft Corporation and Mark Russinovich. MIT license."
''', encoding="utf-8")
    (source / "branding.h").write_text('#define ZOOMIT_PRODUCT_NAME "ZoomIt Muted Green (unofficial)"\n', encoding="utf-8")

    deps = work / "packages"
    deps.mkdir()
    for name, version in PACKAGES.items():
        archive = deps / f"{name}.{version}.nupkg"
        url = f"https://api.nuget.org/v3-flatcontainer/{name.lower()}/{version}/{name.lower()}.{version}.nupkg"
        urllib.request.urlretrieve(url, archive)
        folder = deps / name
        with zipfile.ZipFile(archive) as zipped:
            zipped.extractall(folder)
            notices = [n for n in zipped.namelist() if not n.endswith("/") and ("license" in Path(n).name.lower() or "notice" in Path(n).name.lower())]
            if not notices:
                raise RuntimeError(f"ライセンス文書が見つかりません: {name}")
            for n in notices:
                target = licenses / name / n
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(zipped.read(n))
        print(f"依存ライブラリ: {name} {version}; SHA256={hashlib.sha256(archive.read_bytes()).hexdigest()}", flush=True)

    generated = work / "generated"
    run(deps / "Microsoft.Windows.CppWinRT/bin/cppwinrt.exe", "-input", "sdk", "-output", generated)
    wil = next((deps / "Microsoft.Windows.ImplementationLibrary").rglob("wil/resource.h")).parent.parent
    robmikh = next((deps / "robmikh.common").rglob("robmikh.common/DesktopWindow.h")).parent.parent
    includes = [source, common, generated, wil, robmikh]
    compile_args = ["cl.exe", "/nologo", "/c", "/O2", "/MT", "/EHsc", "/std:c++20", "/utf-8", "/bigobj", "/DUNICODE", "/D_UNICODE", "/DNDEBUG", "/DWINVER=0x0A00", "/D_WIN32_WINNT=0x0A00", "/D_CRT_SECURE_NO_WARNINGS"]
    compile_args += [f"/I{p}" for p in includes]
    files = [source / n for n in ("AudioSampleGenerator.cpp", "CaptureFrameWait.cpp", "SelectRectangle.cpp", "Utility.cpp", "DemoType.cpp", "VersionHelper.cpp", "VideoRecordingSession.cpp", "Zoomit.cpp")]
    files += [common / "WindowsVersions.cpp", common / "dll.c"]
    (work / "verify_color.cpp").write_text('#include "pch.h"\n#include "ZoomIt.h"\nstatic_assert(COLOR_GREEN == RGB(107, 158, 120));\n', encoding="utf-8")
    files.append(work / "verify_color.cpp")
    run(*compile_args, *files, cwd=work)
    run("rc.exe", "/nologo", "/d_M_X64", f"/i{source}", f"/fo{work / 'ZoomIt.res'}", source / "ZoomIt.rc", cwd=source)
    exe = package / "ZoomIt-MutedGreen.exe"
    libraries = ["user32", "gdi32", "advapi32", "shell32", "ole32", "oleaut32", "uuid", "shlwapi", "comctl32", "version", "winmm", "gdiplus", "msimg32", "uxtheme", "windowsapp", "runtimeobject", "dwmapi"]
    run("link.exe", "/nologo", "/SUBSYSTEM:WINDOWS", "/MACHINE:X64", "/MANIFEST:NO", "/DYNAMICBASE", "/NXCOMPAT", f"/OUT:{exe}", *sorted(work.glob("*.obj")), work / "ZoomIt.res", *[f"{n}.lib" for n in libraries], cwd=work)

    # このビルドのプロセスだけを起動して、初期化直後の異常終了がないことを確認。
    process = subprocess.Popen([str(exe)])
    try:
        time.sleep(5)
        if process.poll() is not None:
            raise RuntimeError(f"起動確認に失敗しました: {process.returncode}")
        print("起動確認: 5秒間、異常終了なし", flush=True)
    finally:
        if process.poll() is None:
            process.terminate()
            process.wait(timeout=10)

    script_dir = Path(__file__).resolve().parent
    shutil.copy2(script_dir / "使い方.txt", package / "使い方.txt")
    (package / "SOURCE.txt").write_text(
        f"公開ソース: https://github.com/microsoft/PowerToys/tree/{UPSTREAM_COMMIT}\n"
        "PowerToys v0.90.1内のZoomIt 9.0を単体ビルド。緑を#6B9E78へ変更。\n"
        "MITライセンス文書を同梱し、Sysinternalsバイナリ用のEULA表示を除外。\n"
        "非公式版を示すタイトル・バージョン情報を設定。Microsoftの署名なし。\n"
        "ソースとビルド方法: https://github.com/juyeongjung1/vue3/tree/main/tools/zoomit/portable\n"
        + "\n".join(f"{n} {v}" for n, v in PACKAGES.items()) + "\n", encoding="utf-8-sig")
    with zipfile.ZipFile(package / "source.zip", "w", zipfile.ZIP_DEFLATED) as zipped:
        for folder in (source, common):
            for path in sorted(folder.rglob("*")):
                if path.is_file():
                    zipped.write(path, path.relative_to(work))
        zipped.write(upstream / "LICENSE", "LICENSE.txt")
        zipped.write(Path(__file__), "build.py")
    digest = hashlib.sha256(exe.read_bytes()).hexdigest()
    (package / "SHA256SUMS.txt").write_text(f"{digest}  {exe.name}\n", encoding="ascii")
    output = shutil.make_archive(str(work / package.name), "zip", work, package.name)
    print(f"配布ZIPを作成しました: {output}", flush=True)


if __name__ == "__main__":
    main()
