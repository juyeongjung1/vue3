<script setup lang="ts">
import { ref } from 'vue'

// a. ステータス変数の定義
// •	boolean 型の変数 isOnline（初期値 true）を ref で定義してください。


/* b. 切り替え関数の実装
  changeWorkStatus 関数を作成し、isOnline の値を反転（true ⇔ false）させてください。*/

const changeWorkStatus = () :void => {
  

} 

</script>

<template>
  <h1>演習2-4-2</h1>
  <hr>
 <!-- c. 表示の出し分け（v-if と v-else）
•	v-if / v-else を使い、以下の表示を切り替えてください。
o	isOnline が true の場合: 「現在、業務中です」
o	isOnline が false の場合: 「現在、離席しています」 -->

  <div>
    <p>現在、業務中です</p>
  </div>
  <div>
    <p>現在、離席しています</p>
  </div>

<!-- d. 補足メッセージの表示（v-show）
•	v-show ディレクティブを使い、isOnline が false（離席中）の時だけ
  表示される以下のメッセージを追加してください。
o	メッセージ: 「※緊急の連絡は電話でお願いします」 -->
  <p                class = "text-danger">
    
  </p>

  <button @click="changeWorkStatus() ">状態切り替え</button>
</template>