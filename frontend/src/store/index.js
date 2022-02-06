import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    access: '',
    refresh: ''
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('access') && localStorage.getItem('refresh')) {
        state.access = localStorage.getItem('access')
        state.refresh = localStorage.getItem('refresh')
        state.isAuthenticated = true
      }
    },
    setJWT(state) {
      state.access = localStorage.getItem('access')
      state.refresh = localStorage.getItem('refresh')
      state.isAuthenticated = true
    },
    remJWT(state) {
      state.access = ''
      state.refresh = ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
