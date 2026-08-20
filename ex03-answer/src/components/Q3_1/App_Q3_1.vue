<script setup lang="ts">
/* b. 親コンポーネントでの組み立て (App_Q3_1.vue)
 script setup で上記4つのコンポーネントをインポートしてください。
 例）Header.vueの住所は、./Header.vue です。*/

import Header from './Header.vue'
import Main from './Main.vue'
import SideMenu from './SideMenu.vue'
import Footer from './Footer.vue'
</script>

<template>
  <Header /> <!-- ヘッダーコンポーネントの配置 -->
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <SideMenu /> <!-- サイドメニューコンポーネントの配置 -->
      </div>
      <div class="col-md-9"> 
        <Main /> <!-- メインコンテンツの配置 -->
      </div>
    </div>
  </div>
  <Footer /> <!-- フッターコンポーネントの配置 -->
</template>