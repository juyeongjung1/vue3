<script setup lang="ts">
import { reactive } from 'vue'

/*a a. データの定義（演習2.3.2のソースコードに追記）
　photoUrl: '/images/photo1.png'　を追記
　textColor: 'black'　を追記*/
const employee = reactive({
  name: '田中 太郎',
  department: '開発部',
  workLocation: '未設定'
 
})

/*b. 更新関数の実装
changeOfficeWork 関数に以下のように追記してください。：
　写真を '/images/photo2.png' に変更
　文字色クラスを 'text-primary'（青色）に変更*/
const changeOfficeWork = () => {
  employee.workLocation = '新宿オフィス'
  

}
/*changeRemoteWork 関数に以下のように追記してください。：
　写真を '/images/photo3.png' に変更
　文字色クラスを 'text-primary'（青色）に変更*/
const changeRemoteWork = () => {
  employee.workLocation = '在宅勤務'
 

}
</script>

<template>
  <h1>演習2-4-1</h1>
  <h2>あなたの情報</h2>
  <!--c. 画面表示（v-bind の適用）
    以下の要素に v-bind（または :）を適用してください。
    o	img タグの src 属性 → employee.photoUrl
    o	出勤場所を表示する p タグの class 属性 → employee.textColor-->

  <div><img           alt="プロフィール画像" width="150" height="200"></div>
  <p>氏名：{{ employee.name }}</p>
  <p>部署：{{ employee.department }}</p>
  <p                  >出勤場所：{{ employee.workLocation }}</p>

  <hr>
  <h3>本日の出勤場所</h3>
  <!--「オフィス」ボタンと「リモートワーク」ボタンは、実装済み-->
  <button @click="changeOfficeWork">オフィス</button>
  <button @click="changeRemoteWork">リモートワーク</button>

</template>
