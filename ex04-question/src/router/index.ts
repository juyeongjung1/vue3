
//b. ルーター設定ファイルの作成 (src/router/index.ts)
// Vue Router の機能をインポートしています
import { createRouter, createWebHistory } from 'vue-router'

import Dummy from '../views/Q4_3/Dummy.vue' // エラー防止のためのダミーインポート

/*➀ HomeView と EmployeeListView コンポーネントをインポートしてください。
import先のURLは、../views/Q4_3/HomeView.vue と ../views/Q4_3/EmployeeListView.vue です。*/



/*➁ routes 配列に、以下のパスを追記してください。（ダミーは無視）

*/
const routes = [{ path: '/Q4_3/', name: 'homeQ4_3', component: Dummy }, // ダミー設定

  //ここに、, {   } の形でパスを追記してください。
  //path: '/Q4_3' → component: HomeViewQ4_3
  //path: '/Q4_3/employees' → component: EmployeeListViewQ4_3




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
