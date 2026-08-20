
//b. ルーター設定ファイルの作成 (src/router/index.ts)
// Vue Router の機能をインポートしています
import { createRouter, createWebHistory } from 'vue-router'

/*➀ HomeView と EmployeeListView コンポーネントをインポートしてください。
import先のURLは、../views/Q4_3/HomeView.vue と ../views/Q4_3/EmployeeListView.vue です。*/
import HomeViewQ4_3 from '../views/Q4_3/HomeView.vue'
import EmployeeListViewQ4_3 from '../views/Q4_3/EmployeeListView.vue'
import HomeViewQ4_4 from '../views/Q4_4/HomeView.vue'
import EmployeeListViewQ4_4 from '../views/Q4_4/EmployeeListView.vue'
import HomeViewQ4_5 from '../views/Q4_5/HomeView.vue'
import EmployeeListViewQ4_5 from '../views/Q4_5/EmployeeListView.vue'
import HomeViewQ4_6 from '../views/Q4_6/HomeView.vue'
import EmployeeDetailViewQ4_6 from '../views/Q4_6/EmployeeDetailView.vue' 
import EmployeeListViewQ4_6 from '../views/Q4_6/EmployeeListView.vue'

/*➁ routes 配列を定義し、以下のパスを設定します。
path: '/Q4_3' → component: HomeViewQ4_3
path: '/Q4_3/employees' → component: EmployeeListViewQ4_3

※演習4.4以降も、同じく追加分を反映してください。*/


const routes = [
  { path: '/Q4_3/', name: 'homeQ4_3', component: HomeViewQ4_3 },
  { path: '/Q4_3/employees', name: 'employeesQ4_3', component: EmployeeListViewQ4_3},
  { path: '/Q4_4/', name: 'homeQ4_4', component: HomeViewQ4_4 },
  { path: '/Q4_4/employees', name: 'employeesQ4_4', component: EmployeeListViewQ4_4},
  { path: '/Q4_5/', name: 'homeQ4_5', component: HomeViewQ4_5 },
  { path: '/Q4_5/employees', name: 'employeesQ4_5', component: EmployeeListViewQ4_5},
  { path: '/Q4_6/employees', name: 'employeesQ4_6', component: EmployeeListViewQ4_6},
  { path: '/Q4_6/', name: 'homeQ4_6', component: HomeViewQ4_6 },
  { path: '/Q4_6/employees/:id', name: 'employeeDetailQ4_6', component: EmployeeDetailViewQ4_6}
 
]

// ルーターを作成
const router = createRouter({
  // ブラウザの履歴管理を有効に、基本URLをvite.config.tsのBASE_URLを基準に設定
  history: createWebHistory(import.meta.env.BASE_URL),
  routes                        // 上で定義したルート情報を登録
})

// 他のファイル（main.tsなど）で使えるようにエクスポート
export default router
