# ZoomIt 7.20の緑を落ち着いた色に変更

## 他のPCへ渡す配布版

`portable/build.py` と `.github/workflows/zoomit-portable.yml` で、MITライセンスの公開ソースからWindows x64用のZIPを作成します。PowerToys v0.90.1に含まれるZoomIt 9.0（コミット `229a2894fa27c3a879132bd013f05951d4523660`）を使用し、緑を `#65C155`（RGB: 101, 193, 85）に変更します。

配布ZIPには実行ファイル、日本語の使い方、ライセンス文書、変更済みソースを同梱します。Sysinternals版7.20の実行ファイルは含めません。非公式ビルドであり、Microsoftの電子署名はありません。

配布版9.0.0.3は、初回配布版と同じ `HKEY_CURRENT_USER\Software\Sysinternals\ZoomIt` の設定を引き継ぎます。元のZoomItを終了してから起動してください。以前の色が復元された場合は、描画モードで文字入力を始める前にGを押すと、新しい緑に切り替わって保存されます。

ビルドはGitHub Actionsの「ZoomItの配布用ZIPを作成」から実行できます。ローカルで再ビルドする場合は、Visual Studio 2022のx64 Native Tools環境、Windows SDK、Pythonを用意し、上記コミットのPowerToysを取得してから次を実行します。

```powershell
python -X utf8 tools/zoomit/portable/build.py "PowerToysの取得先" "新規ビルドフォルダー"
```

ソースと依存ライブラリを取得するため、ビルド時にはインターネット接続が必要です。受け取った人のPCにはPythonや開発ツールは不要です。

## 手元の7.20を変更するスクリプト

`set_muted_green.py` は、確認済みの64ビット版ZoomIt 7.20について、緑の色指定を `#00FF00` から `#6B9E78`（RGB: 107, 158, 120）へ変更したコピーを作ります。

対象ファイルをSHA256で照合するため、別バージョンには適用できません。Pythonの標準ライブラリのみを使用します。

```powershell
python -X utf8 tools/zoomit/set_muted_green.py "元のZoomIt64.exe" "変更版ZoomIt64.exe"
```

元ファイルや既存の出力先は上書きしません。実行ファイル自体はリポジトリに含めません。

## 変更箇所と検証

- 元ファイルのSHA256: `67f2e8d935b1d207c62915d7a6a8f74b2ea95ba5bc3c81b309ac39c57609f59b`
- 変更版のSHA256: `e3c3bfc69d4ea6056088c1269593495f4b873db50f0ea1a5cb679ad3f8835d3a`
- ファイルサイズ: 698,288バイト（変更なし）
- 緑キーを判定する `cmp rbx, 0x47` の分岐内、ファイルオフセット `0x1ED7D` の `mov dword ptr [rdi], 0xff00` を `mov dword ptr [rdi], 0x789e6b` に変更。
- WindowsのCOLORREFは `0x00BBGGRR` 形式。差分は `0x1ED7F`〜`0x1ED81` の色の即値3バイトのみ。
- 逆アセンブルと全バイト比較で、他の命令が変わらないことを確認。
- 対象外ファイルの拒否と、既存出力ファイルの上書き拒否を確認。

この色指定は文字・ペン・休憩タイマーの緑で共有されています。
変更版は起動・常駐を確認しました。描画画面を自動操作ツールが取得できなかったため、Ctrl+Gによる文字色の目視確認は未実施です。

## 2026年10月23日の反映と復元

指定されたダウンロードフォルダー内の `ZoomIt/ZoomIt64.exe` と、実際に常駐していた `ZoomIt (1)/ZoomIt64.exe` が同じファイルであることを確認し、両方に反映しました。常駐は従来と同じ `ZoomIt (1)` 側から再起動しています。

それぞれのフォルダーに元ファイルを `ZoomIt64.original-7.20.exe.bak` として保存しました。元に戻す場合はZoomItを終了し、そのバックアップを `ZoomIt64.exe` にコピーしてから起動してください。

変更版ではMicrosoftの電子署名が無効になります。バックアップは元のハッシュと有効な署名を保持しています。公式版への更新・上書き後は元の配色に戻り、このスクリプトは異なるファイルには適用できません。
