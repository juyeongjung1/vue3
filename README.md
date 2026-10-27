# Vue 3 講座の教材

## 配布用の軽量版

配布用ZIPには、指定したコミットの教材・問題・解答・画像・PDF資料を収録します。`package.json` と `package-lock.json`、APIのデータベースも残します。容量の大きい `Text` 内の編集用Word文書（`.docx`）は除外します。

ローカルの作業中の修正、未コミットの追加ファイル、`node_modules`、Gitの履歴（`.git`）は含めません。教材のソースを編集して実行するための配布物です。

### 受け取った方の使い方

1. ZIPを展開します。
2. Node.jsとnpmを用意します。教材のVite 7に対応するNode.js 22.12以降の22系を使用できます。
3. 使用する教材フォルダーで、次を実行します。

```powershell
cd ch01-setup
npm ci
npm run dev
```

`npm ci`にはインターネット接続が必要です。使用するフォルダーごとに一度実行してください。起動後に表示されるURLをブラウザーで開きます。終了は `Ctrl+C` です。

第5章のAPIを使う場合は、別のターミナルで `ch05-crud-api`、演習第5章の場合は `ex05-api-answer` に移動し、同じく `npm ci` と `npm run dev` を実行します。APIはどちらもポート3000を使用するため、使用する方だけを起動してください。

### 配布者向け：ZIPの再作成

Git、Python 3を用意し、リポジトリのルートで実行します。

```powershell
git fetch origin
python tools/create_distribution.py
```

GitHubから取得した `origin/main` の確定済みコミットを使い、`distribution/vue3-course-コミットID.zip` を作成します。**手元の未コミットの修正は入りません。** 除外するWord文書のGit LFSデータはダウンロードしません。配布対象に別のGit LFSポインターが見つかった場合は、実体のないファイルを配らないよう作成を中止します。

過去の完成版を指定する場合は、コミットIDまたはタグを渡します。

```powershell
python tools/create_distribution.py --ref コミットID
```

既存のZIPは上書きしません。`--output 別のファイル名.zip` で保存先を変更できます。生成したZIPはGitにコミットせず、そのまま配布してください。
