<script setup lang="ts">
// ➀ ここに、reactive関数をインポートしてください


// ➁　ここに、reactive関数で複数プロパティをまとめてリアクティブな変数を作成してください。
// 初期値は以下の通りとしてください
// { id: 1, name: 'ノートパソコン', price: 50000 }


// ➂　以下のコメント解除を行ってください。リアクティブ変数の値を変動させる関数です。

// const raisePrice = () => {　// 価格を上げる関数
//   product.price += 1000　// reactiveで作成した変数は、.value不要で直接アクセスできる
// }

// const rename = () => {　// 名前を更新する関数
//   product.name += ' (New)'; 
// }

</script>

<template>
  <h3>商品情報</h3>
  <ul>
    <!-- ➃ <li></li>内に、マスタッシュ構文を使って、➁の変数の各プロパティを表示してください -->
    <li>商品番号：</li>
    <li>商品名　：</li>
    <li>価格　　：</li>
  </ul>

<!-- ➄ 以下のコメント解除をしてください。ボタンクリックしたら動作確認用の関数を実行します。 -->
  <!-- <button @click="raisePrice">価格 +1000</button>
  <button @click="rename">名前を更新</button> -->
</template>
