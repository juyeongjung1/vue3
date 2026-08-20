<script setup lang="ts">

import HeaderMenu from './components/HeaderMenu.vue'
//【3.1 ➀】　ここに、他の3つのコンポーネントをインポートするコードを追加してください

//【ここからは、3.2で利用する枠】
   //【3.2 ➀】　以下に、HeaderMenuに渡すデータを定義してください。変数名は、titleとuserNameです。



   //【3.2 ➁】　以下のMainContentで利用する商品一覧データを確認してください。

const products = [
  { id: 1, name: 'ノートパソコン', price: 120000, category: '電子機器' },
  { id: 2, name: 'スマートフォン', price: 90000, category: '電子機器' },
  { id: 3, name: 'オフィスチェア', price: 25000, category: '家具' },
  { id: 4, name: 'ボールペンセット', price: 800, category: '文房具' }
]
//【ここまでは、3.2で利用するデータ】


//【3.3 ➃】 以下に、子コンポーネントからの通知とIDを受け取る関数を作成してください。


</script>

<template>
  <div class="container-fluid bg-light">
    <!-- 【3.1 ➁】　ここに、HeaderMenu.vueを配置してください-->

    <!--【3.2 ➂】　↑に、3.2 ➀で定義したデータを渡すように修正してください -->

    <div class="container my-4">
      <div class="row">
        <div class="col-md-3">

          <!-- 【3.1 ➂】　ここに、SideMenu.vueを配置してください-->

        </div>
        <div class="col-md-9">

          <!-- 【3.1 ➃】　ここに、MainContent.vueを配置してください-->
          
          <!--【3.2 ➃】　↑に、3.2 ➁で定義したデータを渡すように修正してください -->

           <!--【3.3 ➄】　↑に、子コンポーネントで定義したイベントを受け取るように修正してください -->

           
        </div>
      </div>
    </div>

    <!-- 【3.1 ➄】ここに、FooterInfo.vueを配置してください-->

  </div>
</template>
<style scoped>

</style>