import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Search from '../views/Search.vue'
import Icon from '../views/Icon.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/icon/:slug/',
    name: 'Icon',
    component: Icon,
  },
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router
