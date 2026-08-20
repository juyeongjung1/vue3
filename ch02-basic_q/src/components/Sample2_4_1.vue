<script setup lang="ts">
import { reactive } from 'vue'

//➀ 以下の、reactive関数を使ったリアクティブ変数を確認してください。
// 以下が初期画面に表示される値となります。
const locationInfo = reactive({
  name: '東京会場',
  imagePath: '/images/sample1.jpg',
  linkUrl: 'https://www.trainocate.co.jp/guide/tokyo.html',
  buttonClass: 'btn btn-primary',
  state: 1
})

// ➁ 以下の、状態を切り替える関数を確認してください。
// 特に、stateによる条件分岐と、各プロパティの更新部分を確認してください。
// buttonClassの部分も注目してください。

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
　<!--➂ ここに、locationInfoの会場名をマシュッタシュ文で書いてください。-->
    <h3>{{      }}の情報</h3> 
    
    <!-- ➃ ここに、ディレクティブ構文でsrc属性を設定してください。-->
    <img                                 alt="会場画像" width="200" class="mb-3">

  
    <p>
      <!-- ➄ ここに、ディレクティブ構文でhref属性を設定してください。-->
      <a                                   target="_blank">
        会場の詳細サイトを開く
      </a>
    </p>

    <!-- ➅ ここに、ディレクティブ構文でclass属性を設定してください。-->
    <button                                      @click="toggle">
      別の会場を確認する
    </button>
</template>
