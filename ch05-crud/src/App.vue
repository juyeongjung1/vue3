<script setup lang="ts">
import HeaderMenu from './components/HeaderMenu.vue'
import SideMenu from './components/SideMenu.vue'
import FooterInfo from './components/FooterInfo.vue'
</script>

<template>
  <!-- ※補足：min-vh-100 と d-flex flex-column により、内容が少ない画面でもフッターを画面下部へ配置します。 -->
  <div class="container-fluid bg-light min-vh-100 d-flex flex-column p-0">
  
    <HeaderMenu />

    <div class="container my-4 flex-grow-1">
      <div class="row">
        <div class="col-md-3">
          <SideMenu />
        </div>
        <div class="col-md-9">
          <!-- ルーティングされたコンポーネントがここに表示される -->
          <RouterView />　
        </div>
      </div>
    </div>
    <FooterInfo />
  </div>
</template>
