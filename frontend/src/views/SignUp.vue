<template>
  <div class="page-sign-up">

    <div class="columns">
      <div class="column is-4 is-offset-4">

        <h1 class="title">Sign up</h1>
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
          <div class="field">
            <label>Repeat password</label>
            <div class="control">
              <input type="password" class="input" v-model="password2">
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark">Sign up</button>
            </div>
          </div>

          <hr>
          Or <router-link to="/log-in">click here</router-link> to log in!

        </form>

      </div>
    </div>

  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'SignUp',
    data() {
      return {
        'email': '',
        'password': '',
        'password2': '',
        'errors': []
      }
    },
    methods: {
      submitForm() {
        this.errors = []

        if (this.email === '') {
          this.errors.push('E-mail is missing')
        }
        if (this.password === '') {
          this.errors.push('Password is too short')
        }
        if (this.password !== this.password2) {
          this.errors.push('Passwords don\'t match')
        }

        if (!this.errors.length) {
          const formData = {
            email: this.email,
            password: this.password
          }
          axios
            .post("http://127.0.0.1:8000/auth/users/", formData)
            .then(response => {
              console.log(response.data)
              this.$router.push('/log-in')
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
          // axios ( without {} )
        }
      }
    }
  }
</script>
