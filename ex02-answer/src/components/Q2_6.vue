<script setup lang="ts">
import { reactive } from 'vue'

/*a. フォームデータの定義
•	reactive を使い、以下のプロパティを持つオブジェクト form のソースコードを確認してください。*/
const form = reactive({
  name: '', //氏名
  department: '営業部', //部署
  employmentType: '正社員', //雇用形態
  skills: [] as string[] //所持スキル (チェックボックス用の配列)
})
</script>

<template>
  <h1>演習2-6: 社員登録</h1>
  <hr>
  <!-- b. 入力フォームの作成
　以下のフォーム要素を作成し、v-model で form の各プロパティとバインドしてください。 -->

  <!-- 氏名入力 -->
  <div>
    <label>氏名: </label>
    <input type="text" v-model="form.name"> <!-- ここにform.nameを双方向バインディングする -->
  </div>
  <br>

  <!-- 部署選択 -->
  <div>
    <label>部署: </label>
    <select v-model="form.department"> <!-- ここにform.departmentを双方向バインディングする -->
      <option>営業部</option>
      <option>開発部</option>
      <option>総務部</option>
    </select>
  </div>
  <br>

  <!-- 雇用形態選択（ラジオボタン） -->
  <div>
    <label>雇用形態: </label>
    <!--※ ラジオボタンは、同じ v-model を指定することでグループ化されます。 -->
    <label>
      <input type="radio" value="正社員" v-model="form.employmentType"> 正社員 
    </label>
    <label>
      <input type="radio" value="契約社員" v-model="form.employmentType"> 契約社員
    </label>
    <label>
      <input type="radio" value="パート" v-model="form.employmentType"> パート
    </label>
  </div>
  <br>

  <!-- スキル選択（チェックボックス） -->
  <div>
    <label>所持スキル: </label>
    <label>
      <!-- チェックボックスは、value 属性にスキル名を設定し、v-model で同じ配列（form.skills）にバインドします。 -->
      <input type="checkbox" value="Java" v-model="form.skills"> Java
    </label>
    <label>
      <input type="checkbox" value="Vue.js" v-model="form.skills"> Vue.js
    </label>
    <label>
      <input type="checkbox" value="Python" v-model="form.skills"> Python
    </label>
  </div>
  <hr>
  <!-- c. 入力内容の確認表示
•	入力された値をリアルタイムで表示するエリアを作成してください。 -->
  <div>
    <h3>登録内容プレビュー</h3>
    <p>氏名: {{ form.name }}</p>
    <p>部署: {{ form.department }}</p>
    <p>雇用形態: {{ form.employmentType }}</p>
    <p>スキル: {{ form.skills }}</p>
  </div>
</template>
