# 第 5 章 演習ガイド：コンポーネントのライフサイクルと API 連携

## 演習の目標
- **Axios** を使用して REST API との通信（データの取得・送信）ができる
- **ライフサイクルフック (onMounted)** を利用して、初期表示時にデータを読み込める
- **リストレンダリング (v-for)** と **RouterLink** を組み合わせて、データに基づいたページ遷移を実装できる
- **CRUD 処理**（一覧・詳細・作成・更新・削除）の基本的な流れを理解できる
- **双方向データバインディング (v-model)** を使用して、フォームデータを処理できる

## 演習の概要
第 5 章で学習した API 連携と非同期処理の手法を実践します。本演習では、あらかじめ用意されたバックエンド（**ex05-api-answer**）の REST API を使用して、社員情報の取得・登録・更新・削除を行います。

**プロジェクト名: ex05-question**

**使用する API サーバー: ex05-api-answer (http://localhost:3000)**

## 予想所要時間
約 60 分


## 演習 5.1. 社員一覧の表示

`src/views/EmployeeListView.vue` を編集し、API から社員情報を取得して一覧表示する機能を実装してください。

### 作業の前提:
*   Vue-router、axiosモジュールは、npmから導入済みです。
*   3章で作成した `Header.vue`, `SideMenu.vue`, `Footer.vue` が `src/components` 内に存在している状態から開始します。
*   REST APIのソースコードは、`ex05-api-answer`の「`server.js`」を参照してください。

### 作成・修正するファイル:
*   `src/views/EmployeeListView.vue`

**a. Axios のインポート（EmployeeListView.vue）**
*   ➀ `script setup` 内で、`axios` をインポートしてください。
*   ➁ `script setup` 内で、`keyword` を保持する ref 変数を定義してください（初期値は空文字）。

**b. 全件取得関数の実装（EmployeeListView.vue）**
*   `fetchEmployees` 関数を定義し、`axios.get` を使用して全社員情報を取得してください。
    *   利用 API: **1.B 全件取得 API (GET)**
    *   URL: `http://localhost:3000/api/employees/`

**c. マウント時の処理（EmployeeListView.vue）**
*   画面初期表示時 (`onMounted`) に `fetchEmployees` 関数を実行してください。

**d. 検索用変数の定義（EmployeeListView.vue）**
*   `keyword` を保持する ref 変数を定義してください（初期値は空文字）。

**e. 検索機能の実装（EmployeeListView.vue）**
*   `searchEmployees` 関数を定義し、`axios.get` を使用して検索結果を取得してください。
    *   利用 API: **1.A 検索 API (GET)**
    *   URL: `http://localhost:3000/api/employees/search?keyword=...`

**f. 双方向バインディング（EmployeeListView.vue）**
*   `template` 内で記述します。
*   input タグと `keyword` 変数を双方向データバインディングしてください。

**g. リストレンダリング（EmployeeListView.vue）**
*   `template` 内で記述します。
*   `v-for` を使用して employees の内容を繰り返し表示してください。

**h. 詳細リンク（EmployeeListView.vue）**
*   `template` 内で記述します。
*   `RouterLink` を使用して、社員詳細画面（`/employees/ID`）へのリンクを作成してください。

### 【動作確認 5.1】
1.  API サーバーを起動します (`ex05-api-answer` で `node server.js`)。
2.  開発サーバーを起動します (`ex05-question` で `npm run dev`)。
3.  トップページにアクセスし、社員一覧が表示されるか確認します。
4.  検索ボックスに「山田」などのキーワードを入力し、「検索」ボタンをクリックして検索が動作するか確認します。


## 演習 5.2. 社員詳細の表示と削除

### 作成・修正するファイル:
*   `src/views/EmployeeDetailView.vue`

**a. Axios のインポート（EmployeeDetailView.vue）**
*   `script setup` 内で、`axios` をインポートしてください。

**b. 詳細取得（EmployeeDetailView.vue）**
*   `axios.get` を使用して、特定の社員情報を取得してください。
    *   利用 API: **2. 社員詳細取得 API (GET)**
    *   URL: `http://localhost:3000/api/employees/ID/`

**c. 削除機能（EmployeeDetailView.vue）**
*   ➀ `axios.delete` を使用して、特定の社員データを削除してください。
    *   利用 API: **5. 社員削除 API (DELETE)**
    *   URL: `http://localhost:3000/api/employees/ID/`
*   ➁ 削除完了後、一覧画面にリダイレクトさせるロジックも検討してください。

**d. 画像表示制御（EmployeeDetailView.vue）**
*   `template` 内で記述します。
*   `image_path` がある場合のみ `<img>` タグを表示してください。

**e. 画像パスのバインド（EmployeeDetailView.vue）**
*   `template` 内で記述します。
*   `src` 属性に `image_path` をバインドしてください。

**f. 編集リンク（EmployeeDetailView.vue）**
*   `template` 内で記述します。
*   編集画面（`/employees/edit/ID`）への `RouterLink` を作成してください。

### 【動作確認 5.2】
1.  社員一覧画面から任意の社員名をクリックし、詳細画面へ遷移できるか確認します。
2.  社員情報（名前、給与、画像など）が正しく表示されているか確認します。
3.  「削除」ボタンをクリックし、確認ダイアログの後にデータが削除され、一覧画面に戻るか確認します。


## 演習 5.3. 社員情報の編集

### 作成・修正するファイル:
*   `src/views/EmployeeEditView.vue`

**a. データ取得と初期値設定（EmployeeEditView.vue）**
*   ➀ `script setup` 内で、`axios` をインポートしてください。
*   ➁ `axios.get` を使用してデータを取得し、各 ref 変数に代入してください。
    *   利用 API: **2. 社員詳細取得 API (GET)**
    *   URL: `http://localhost:3000/api/employees/ID/`

**b. 更新処理（EmployeeEditView.vue）**
*   `axios.put` を使用してデータを更新してください。
    *   利用 API: **4. 社員更新 API (PUT)**
    *   URL: `http://localhost:3000/api/employees/ID/`
    *   送信データ: `name`, `password`, `salary`, `location_name`, `image_path`

**c. フォーム送信（EmployeeEditView.vue）**
*   フォーム送信時（submit）に `updateEmployee` を実行するようにしてください。

**d. バインディング（EmployeeEditView.vue）**
*   `template` 内で記述します。
*   各 input タグに適切な `v-model` を設定してください。

### 【動作確認 5.3】
1.  詳細画面の「編集」リンクをクリックし、編集画面へ遷移できるか確認します。
2.  フォームに既存のデータ（名前や給与など）が初期表示されているか確認します。
3.  内容を変更し、「更新」ボタンをクリックして更新が成功するか（詳細画面へ戻り、変更が反映されているか）確認します。


## 演習 5.4. 新規社員の登録

### 作成・修正するファイル:
*   `src/views/NewEmployeeView.vue`

**a. 登録処理（NewEmployeeView.vue）**
*   ➀ `script setup` 内で、`axios` をインポートしてください。
*   ➁ `axios.post` を使用して、新規社員情報を登録してください。
    *   利用 API: **3. 社員登録 API (POST)**
    *   URL: `http://localhost:3000/api/employees/`
    *   送信データ: `name`, `password`, `salary`, `location_name`, `image_path`

**b. 画像パス（NewEmployeeView.vue）**
*   `template` 内で記述します。
*   `image_path` 変数を `v-model` でバインドしてください。

### 【動作確認 5.4】
1.  社員一覧画面の「新規登録」ボタンをクリックし、登録画面へ遷移できるか確認します。
2.  各項目を入力し、「登録」ボタンをクリックして新しい社員が追加されるか確認します。
3.  一覧画面に戻り、追加した社員が表示されているか確認します。
