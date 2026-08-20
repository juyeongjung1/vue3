<script setup lang="ts">
/*a. オブジェクトの定義
vue から reactive をインポートしてください。*/


/*reactive を使い、以下のプロパティを持つ社員情報オブジェクト employee を定義してください。
o	name: '田中 太郎'
o	department: '開発部'
o	workLocation: '未設定'*/


/*b. 更新関数の作成
以下の2つの関数を作成してください。
o	changeOfficeWork: workLocation を '新宿オフィス' に変更する。
o	changeRemoteWork: workLocation を '在宅勤務' に変更する。
※ reactive のプロパティにアクセスする際は .value は不要です。*/


</script>

<template>
    <h1>演習2-3-2</h1>
    <hr>
    <h2>あなたの情報</h2>
  <!--c. 画面表示 以下に、オブジェクト内のデータname, department, workLocationを表示してください。-->
    <p>氏名:   </p>
    <p>部署:   </p>
    <p>出勤場所:   </p>

    <h3>本日の出勤場所</h3>
    <!--•	「オフィス」ボタンと「リモートワーク」ボタンに正しい関数を入れてください。-->
    <button @click="   ">オフィス</button>
    <button @click="   ">リモートワーク</button>
</template>
