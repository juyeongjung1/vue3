<script setup lang="ts">
import { reactive } from 'vue'

// 1つのオブジェクトにまとめて管理
const locationInfo = reactive({
  name: '東京会場',
  imagePath: '/images/sample1.jpg',
  linkUrl: 'https://www.trainocate.co.jp/guide/tokyo.html',
  buttonClass: 'btn btn-primary',
  state: 1
})

// ボタンを押すたびに状態を切り替える関数
const toggle = (): void => {
  if (locationInfo.state === 1) {
    locationInfo.name = '大阪会場'
    locationInfo.imagePath = '/images/sample2.jpg'
    locationInfo.linkUrl = 'https://www.trainocate.co.jp/guide/osaka.html'
    locationInfo.buttonClass = 'btn btn-success'
    locationInfo.state = 2
  } else if (locationInfo.state === 2) {
    locationInfo.name = '名古屋会場'
    locationInfo.imagePath = '/images/sample3.jpg'
    locationInfo.linkUrl = 'https://www.trainocate.co.jp/guide/nagoya.html'
    locationInfo.buttonClass = 'btn btn-warning'
    locationInfo.state = 3
  } else {
    locationInfo.name = '東京会場'
    locationInfo.imagePath = '/images/sample1.jpg'
    locationInfo.linkUrl = 'https://www.trainocate.co.jp/guide/tokyo.html'
    locationInfo.buttonClass = 'btn btn-primary'
    locationInfo.state = 1
  }
}
</script>

<template>

    <h3>{{ locationInfo.name }}の情報</h3>
    
    <!-- v-bind:src → :src で画像を動的に変更 -->
    <img :src="locationInfo.imagePath" alt="会場画像" width="200" class="mb-3">

    <!-- v-bind:href → :href でリンク先を動的に変更 -->
    <p>
      <a :href="locationInfo.linkUrl" target="_blank">
        会場の詳細サイトを開く
      </a>
    </p>

    <!-- v-bind:class → :class でBootstrapボタンの色を動的に変更 -->
    <button :class="locationInfo.buttonClass" @click="toggle">
      別の会場を確認する
    </button>
</template>
