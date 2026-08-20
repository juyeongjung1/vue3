<script setup lang="ts">
import { ref, reactive } from 'vue'

//➀　以下のデータ群を確認してください。

// カウント値
const count = ref(0)

// 選択された商品の情報
const selected = ref('')

// マウスオーバー時のメッセージ
const hoverMsg = ref('（ボタンにマウスを乗せてみてください）')

// 商品リスト
const products = reactive([
  { id: 1, name: 'ノートパソコン', price: 120000 },
  { id: 2, name: 'マウス', price: 2500 },
  { id: 3, name: 'キーボード', price: 4800 }
])

//➁　以下のメソッド群を確認してください。

// カウントを増やすメソッド
const increment = (): void => {
  count.value++
}

// カウントをリセットするメソッド
const reset = (): void => {
  count.value = 0
}

// マウスが乗ったときのメソッド
const onMouseOver = (): void => {
  hoverMsg.value = 'マウスが乗りました！'
}

// マウスが離れたときのメソッド
const onMouseOut = (): void => {
  hoverMsg.value = '（ボタンにマウスを乗せてみてください）'
}

//➂ 以下の引数付きメソッドを確認してください。

// 商品がクリックされたとき（引数あり）のメソッド
const selectProduct = (name: string, price: number): void => {
  selected.value = `選択した商品：${name}（${price}円）`
}

</script>

<template>
  <div class="text-center">
    <h3>イベント処理（v-on）</h3>

    
   
    <p>現在のカウント：{{ count }}</p>
     <!-- ➃　以下のボタンに、上記のメソッド名を参照し、適切なクリックイベントを追加してください。 -->
    <button class="btn btn-primary mx-1"               >増やす</button>
    <button class="btn btn-secondary mx-1"             >リセット</button>

    <hr class="my-4" />

    <h5>マウス操作のイベント</h5>
    <!-- ➄　以下のボタンに、上記のメソッド名を参照し、mouseover/mouseoutイベントを追加してください。 -->
    <button class="btn btn-success"                  >ホバーしてみよう</button>
    <p class="mt-2">{{ hoverMsg }}</p>

    <hr class="my-4" />
    
    <h5>商品一覧</h5>
    <table class="table table-bordered w-auto mx-auto">
      <thead class="table-light">
        <tr>
          <th>ID</th>
          <th>商品名</th>
          <th>価格</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in products" :key="p.id">
          <td>{{ p.id }}</td>
          <td>{{ p.name }}</td>
          <td>{{ p.price }}円</td>
          <td>
            <!-- ➅ 以下のボタンに、上記のメソッド名を参照し、行ごとのクリックイベントを追加してください。 -->
            <button class="btn btn-sm btn-outline-primary"                   >選択</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p class="mt-2">{{ selected }}</p>

  </div>
</template>
