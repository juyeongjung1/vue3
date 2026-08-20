<script setup lang="ts">
import HeaderMenu from './components/HeaderMenu.vue'
import SideMenu from './components/SideMenu.vue'
import MainContent from './components/MainContent.vue'
import FooterInfo from './components/FooterInfo.vue'

import { ref } from 'vue'
//【ここからは、3.2で利用するデータ】
// 親で管理するデータ
const pageTitle = '商品管理システム'
const userName = '管理者'

// 商品一覧データ（このあと MainContent に渡す）
const products = ref([
  { id: 1, name: 'ノートパソコン', price: 120000, category: '電子機器' },
  { id: 2, name: 'スマートフォン', price: 90000, category: '電子機器' },
  { id: 3, name: 'オフィスチェア', price: 25000, category: '家具' },
  { id: 4, name: 'ボールペンセット', price: 800, category: '文房具' }
  //【ここまでは、3.2で利用するデータ】
])

// 【3.3】子から通知された「選択ID」を受け取る
const handleSelect = (id: number) => {
  alert(`親で実行しています。\n選択された商品IDは ${id} です。`)
  //【補足】：子コンポーネントから通知されたIDを使って、親コンポーネントのデータを更新、子コンポーネントに反映させる例
  //  const product = products.value[id - 1]
  //   if (product) {
  //     product.name += '!'
  //   }
}

</script>

<template>
  <div class="container-fluid bg-light">
    <!--3.2 親 → 子：タイトルとユーザー名を渡す -->
    <HeaderMenu :title="pageTitle" :user="userName" />

    <!-- グリッドシステムで横並び -->
    <div class="container my-4">
      <div class="row">
        <div class="col-md-3">
          <SideMenu />
        </div>
        <div class="col-md-9">
          <!-- このあとMainContentにも商品一覧を渡す -->
          <!-- <MainContent :products="products"/> -->

          <!--【3.3のサンプルコード】-->
          <MainContent :products="products" @select="handleSelect" />
          
        </div>
      </div>
   
      
    </div>

    <FooterInfo />
  </div>
</template>
<style scoped></style>