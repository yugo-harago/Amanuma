import { createRouter, createWebHistory } from 'vue-router'
import AppHomeView from '../views/HomeView.vue'
import AboutChurchView from '../views/AboutChurchView.vue'
import LinksView from '../views/LinksView.vue'
import NewsView from '../views/NewsView.vue'
import WorshipView from '../views/WorshipView.vue'
import YoutubeThumbnails from '@/components/YoutubeThumbnails.vue';

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: AppHomeView,
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // },
  {
    path: '/about-church',
    name: 'AboutChurchView',
    component: AboutChurchView,
  },
  {
    path: '/links',
    name: 'LinksView',
    component: LinksView,
  },
  {
    path: '/news',
    name: 'NewsView',
    component: NewsView,
  },
  {
    path: '/worship',
    name: 'WorshipView',
    component: WorshipView,
  },
  {
    path: '/latest-video',
    name: 'YoutubeThumbnails',
    component: YoutubeThumbnails,
  },
]

const router = createRouter({
  history: createWebHistory('/'),
  routes,
})

export default router
