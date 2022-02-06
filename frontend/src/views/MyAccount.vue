<template>
  <div class="page-my-account">

    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My account</h1>
      </div>
      <div class="column is-12">
        <button @click="logout()" class="button is-danger">Log out</button>
      </div>
    </div>

  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'MyAccount',
    data() {
      return {}
    },
    mounted() {
      document.title = 'My account'
    },
    methods: {
      logout() {
        axios.defaults.headers.common["Authorization"] = ""

        localStorage.removeItem('access')
        localStorage.removeItem('refresh')

        this.$store.commit('remJWT')
        this.$router.push('/')
      }
    }
  }
</script>
