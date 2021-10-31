<template>
  <div class="page-home box is-rounded">
    <div class="columns is-multiline">


      <div class="column is-12">
        <h1 class="is-size-2 has-text-centered">
          Latest Icons
        </h1>
      </div>


      <div class="column is-3" v-for="icon in latestIcons.results" :key="icon.id">

            <figure class="image is-256x256">
              <img class="is-rounded" :src="icon.get_image">
            </figure>

            <p class="is-size-6 has-text-grey m-2">{{ icon.name }}</p>


          <div class="columns">
            <div class="column is-3 has-text-centered parent">
              <figure class="image is-32x32 is-inline-block">
                <img class="is-rounded" src="https://bulma.io/images/placeholders/32x32.png">
              </figure>
            </div>
            <div class="column has-text-left mt-1">
              <p class="is-size-6 has-text-grey">{{ icon.get_username }}</p>
            </div>
          </div>

      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Home',

    data() {
        return {
            latestIcons: []
        }
    },

    mounted() {
        this.getLatestIcons()
    },

    methods: {
        async getLatestIcons() {
            await axios
            .get('api/v1/icons/')
            .then(response => {
                console.log(response.data)
                this.latestIcons = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    } 
}
</script>
