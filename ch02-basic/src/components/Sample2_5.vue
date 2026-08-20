<script setup lang="ts">
import { ref, reactive } from 'vue'

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

// 商品がクリックされたとき（引数あり）のメソッド
const selectProduct = (name: string, price: number): void => {
  selected.value = `選択した商品：${name}（${price}円）`
}

</script>

<template>
  <div class="text-center">
    <h3>イベント処理（v-on）</h3>

    <!-- ▼ clickイベント -->
    <p>現在のカウント：{{ count }}</p>
    <button class="btn btn-primary mx-1" @click="increment">増やす</button>
    <button class="btn btn-secondary mx-1" @click="reset">リセット</button>

    <hr class="my-4" />

    <!-- ▼ mouseover / mouseoutイベント -->
    <h5>マウス操作のイベント</h5>
    <button class="btn btn-success" @mouseover="onMouseOver" @mouseout="onMouseOut">
      ホバーしてみよう
    </button>
    <p class="mt-2">{{ hoverMsg }}</p>

    <hr class="my-4" />
    <!-- ▼ 引数付きclickイベント -->
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
            <!-- 引数つきでメソッドを呼び出し -->
            <button class="btn btn-sm btn-outline-primary" @click="selectProduct(p.name, p.price)">
              選択
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <p class="mt-2">{{ selected }}</p>

  </div>
</template>
