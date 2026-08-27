
//b. ルーター設定ファイルの作成 (src/router/index.ts)
// Vue Router の機能をインポートしています
import { createRouter, createWebHistory } from 'vue-router'

// 初期状態でエラーを出さないためのダミーです。➁の作業で、このimportを削除してください。
import Dummy from '../views/Q4_3/Dummy.vue'

/*➀ HomeView と EmployeeListView コンポーネントをインポートしてください。
以下の2行をコピーし、行頭の「//」を外してください。*/
// import HomeViewQ4_3 from '../views/Q4_3/HomeView.vue'
// import EmployeeListViewQ4_3 from '../views/Q4_3/EmployeeListView.vue'

const routes = [
  /*➁ 以下のダミールートの「component: Dummy」を「component: HomeViewQ4_3」に置き換えてください。
  置き換えた後は、上にあるDummyのimportも削除してください。*/
  { path: '/Q4_3', name: 'homeQ4_3', component: Dummy },

  /*続けて、以下の行頭の「//」を外し、社員一覧のルートを追加してください。*/
  // { path: '/Q4_3/employees', name: 'employeesQ4_3', component: EmployeeListViewQ4_3 },

  // ※演習4.4以降も、同じく追加分を反映してください。
]




// ルーターを作成
const router = createRouter({
  // ブラウザの履歴管理を有効に、基本URLをvite.config.tsのBASE_URLを基準に設定
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// 他のファイル（main.tsなど）で使えるようにエクスポート
export default router
