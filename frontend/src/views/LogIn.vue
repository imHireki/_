<template>
  <div class="log-in-page">

    <div class="columns">
      <div class="column is-4 is-offset-4">

        <h1 class="title">Log In</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>E-mail</label>
            <div class="control">
              <input type="text" class="input" v-model="email">
            </div>
          </div>
          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password">
            </div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark">Log In</button>
            </div>
          </div>
        </form>

      </div>
    </div>

  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'LogIn',
    data() {
      return {
        email: '',
        password: '',
        errors: [],
      }
    },
    methods: {
      async submitForm() {

        const formData = {
          email: this.email,
          password: this.password
        }

        await axios
          .post('/auth/jwt/create/', formData)
          .then(response => {
            // Response to variables
            const access = response.data.access
            const refresh = response.data.refresh

            // Set localStorage's JWT
            localStorage.setItem('access', access)
            localStorage.setItem('refresh', refresh)

            // Set state's JWT & isAuthenticated ( using localStorage )
            this.$store.commit('setJWT')

            // Set axios authorization header
            axios.defaults.headers.common["Authorization"] = "JWT " + access

            // Redirect to where were u goin' or home
            const toPath = this.$route.query.to || '/'
            this.$router.push(toPath)
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
              console.log(error.response.data)
            } else if (error.message) {
              this.errors.push('Something went wrong. Please, try again.')
              console.log(error.message)
            }
          })
        }
     }
  }
</script>
