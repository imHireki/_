import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import axios from 'axios'

import Home from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin)) {
    if (store.state.isAuthenticated) {

      let access_exp = JSON.parse(atob(store.state.access.split('.')[1])).exp
      let refresh_exp = JSON.parse(atob(store.state.refresh.split('.')[1])).exp
      let time_now = Number(String(Date.now()).slice(0, 10))

      if (time_now > access_exp ) {
        if (time_now < refresh_exp ) {
          axios
            .post('/auth/jwt/refresh', {"refresh": store.state.refresh})
            .then(response => {
              let access = response.data.access

              localStorage.setItem('access', access)
              axios.defaults.headers.common["Authorization"] = "JWT " + access
              store.commit('setJWT', access, store.state.refresh)

              next()
            })
            .catch(error => {
              next({ name: 'LogIn', query: { to: to.path } })
            })
        } else { next({ name: 'LogIn', query: { to: to.path } }) }
      } else { next() }

    } else { next({ name: 'LogIn', query: { to: to.path } }) }
  } else { next() }
})

export default router
