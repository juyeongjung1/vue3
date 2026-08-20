<script setup lang="ts">
import { ref } from 'vue'

//　➀　以下のリアクティブ変数を確認してください。
const name = ref('')                // テキスト入力
const selectedPrice = ref('3000')   // セレクトボックス
const category = ref('PC')          // ラジオボタン
</script>

<template>
  <div class="text-center">
    <h3>v-model の基本</h3>

    <p>① テキスト入力</p>
    <!--➁　➀を参考にし、の双方向バインディングを適用してください-->
    <input type="text"          placeholder="お名前を入力" class="form-control w-50 mx-auto" />
    <p>こんにちは、{{ name }} さん！</p>

    <hr>

    <!-- セレクトボックス -->
    <p>② セレクトボックス（価格帯）</p>

 <!--➂　➀を参考にし、の双方向バインディングを適用してください-->
    <select             class="form-select w-50 mx-auto">
      <option value="0">指定なし</option>
      <option value="3000">3,000円以上</option>
      <option value="10000">10,000円以上</option>
    </select>
    <p>選択中の価格条件：{{ selectedPrice }}円以上</p>

    <hr>

    <p>③ ラジオボタン（カテゴリ）</p>
    <div>
       <!--➃　➀を参考にし、の双方向バインディングを適用してください-->
      <input type="radio" value="PC"                 /> PC
      <input type="radio" value="Accessory"             /> アクセサリ
      <input type="radio" value="Display"            /> ディスプレイ
    </div>
    <p>選択中のカテゴリ：{{ category }}</p>
  </div>
</template>
