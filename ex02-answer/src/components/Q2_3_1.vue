<script setup lang="ts">
//a. 変数の定義
//vue から ref をインポートしてください。
import { ref } from 'vue'

//文字列型の変数 workState（初期値 '未出勤'）を ref で定義してください。
const workState = ref('未出勤')

/*b. 更新関数の作成
以下の2つの関数を作成してください。
o	workStart: workState の値を '出勤中' に変更する。
o	workEnd: workState の値を '退勤済み' に変更する。
※ script 内で ref の値を操作する際は .value が必要な点に注意してください。
*/
const workStart = () => {
  workState.value = '出勤中'
}

const workEnd = () => {
  workState.value = '退勤済み'
}
</script>

<template>
  <h1>演習2-3-1</h1>
  <hr>
  <!-- c. 画面表示
•	template に以下の要素を配置してください。
o	見出し: <h1>演習2-3-1</h1>
o	現在の状態: <p>勤怠状況: {{ workState }}</p>
o	ボタン: 「出勤する」（クリックで workStart を実行）
o	ボタン: 「退勤する」（クリックで workEnd を実行）
-->
  <p>勤怠状況: {{ workState }}</p>
  <button @click="workStart">出勤する</button>
  <button @click="workEnd">退勤する</button>
</template>
