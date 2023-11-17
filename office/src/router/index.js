import { createRouter, createWebHistory } from 'vue-router'
import AppHomeView from '../views/HomeView.vue'

// import AboutChurchView from '../views/AboutChurchView.vue'
// import LinksView from '../views/LinksView.vue'
import NewsView from '../views/NewsView.vue'
import ArticleView from '../views/ArticleView.vue'
import WorshipView from '../views/WorshipView.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: AppHomeView,
    meta: { requiresAuth: true },  // Add this line
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // },
  // {
  //   path: '/about-church',
  //   name: 'AboutChurchView',
  //   component: AboutChurchView,
  // },
  // {
  //   path: '/links',
  //   name: 'LinksView',
  //   component: LinksView,
  // },
  {
    path: '/news',
    name: 'NewsView',
    component: NewsView,
  },
  {
    path: '/article',
    name: 'ArticvleView',
    component: ArticleView,
  },
  {
    path: '/worship',
    name: 'WorshipView',
    component: WorshipView,
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
  },
]

// const router = new VueRouter({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes
// })

const router = createRouter({
  history: createWebHistory('/office'),
  routes,
})

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem('token')

  if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
    next('/login')
  } else {
    next()
  }
})

export default router
