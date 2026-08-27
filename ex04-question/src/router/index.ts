
//b. ルーター設定ファイルの作成 (src/router/index.ts)
// Vue Router の機能をインポートしています
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'

/*➀ HomeView と EmployeeListView コンポーネントをインポートしてください。
以下の2行をコピーし、行頭の「//」を外してください。*/
// import HomeViewQ4_3 from '../views/Q4_3/HomeView.vue'
// import EmployeeListViewQ4_3 from '../views/Q4_3/EmployeeListView.vue'

const routes: RouteRecordRaw[] = [
  /*➁ 以下の2行をコピーし、行頭の「//」を外してroutes配列にルートを追加してください。*/
  // { path: '/Q4_3', name: 'homeQ4_3', component: HomeViewQ4_3 },
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
