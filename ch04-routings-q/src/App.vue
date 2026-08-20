<script setup lang="ts">
import HeaderMenu from './components/HeaderMenu.vue'
import SideMenu from './components/SideMenu.vue'
import FooterInfo from './components/FooterInfo.vue'
import { ref } from 'vue'
import { provide } from 'vue'

// 親で管理するデータ
const pageTitle = '商品管理システム'
const userName = '管理者'

// 商品一覧データ
const products = ref([
  { id: 1, name: 'ノートパソコン', price: 120000, category: '電子機器' },
  { id: 2, name: 'スマートフォン', price: 90000, category: '電子機器' },
  { id: 3, name: 'オフィスチェア', price: 25000, category: '家具' },
  { id: 4, name: 'ボールペンセット', price: 800, category: '文房具' }
])

// 【4.5 ➀】以下に、他コンポーネント（画面全体）で参照できるように登録してください。

</script>

<template>
  <div class="container-fluid bg-light">
  
    <HeaderMenu :title="pageTitle" :user="userName" />

    <div class="container my-4">
      <div class="row">
        <div class="col-md-3">
          <SideMenu />
        </div>
        <div class="col-md-9">
          <!-- 【4.3 ➂　以下に、RouterViewを配置してください】 -->
          
        </div>
      </div>
    </div>
    <FooterInfo />
  </div>
</template>
<style scoped></style>