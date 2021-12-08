<template>
  <div id="home-page">
    <v-row no-gutters>
      <IconBox
        v-for="icon in icons"
        :key="icon.id"
        :icon="icon"
      >
      </IconBox>
    </v-row>
    <!-- INFINITE SCROLL LOAD -->
    <v-row>
      <v-col class="text-center mt-5">
        <v-progress-circular
          indeterminate
          color="red accent-3"
        ></v-progress-circular>
      </v-col>
    </v-row>
    <!-- / INFINITE SCROLL LOAD -->
  </div>
</template>

<script>
  import axios from 'axios'
  import IconBox from '../components/IconBox.vue'

  export default {
      name: 'Home',
      data() {
        return {
          icons: [],
          page: 1,
          hasNextPage: true,
        }
      },
      components: {
        IconBox
      },
      methods: {
        getIcons() {
          axios
            .get(`http://127.0.0.1:8000/api/v1/icons/?page=${this.page}`)
            .then(response => {
              for (let i = 0; i < response.data.results.length; i++) {
                  this.icons.push(response.data.results[i])
              }
              if (!response.data.next) {
                  this.hasNextPage = false
              }
            }) 
            .catch(error => {
              console.log(error)
            })
        },
        getNextPage() {
          window.onscroll = () => {
            let bottomOfWindow = ( document.documentElement.scrollTop + ( window.innerHeight + ( window.innerHeight * 0.2 ) ) ) >= document.documentElement.offsetHeight

            if (bottomOfWindow && this.hasNextPage) {
              this.page += 1
              this.getIcons()
            }

          }        
        }
      },
      beforeMount() {
        this.getIcons()
      },
      mounted() {
        this.getNextPage()
      }
  }
</script>

<style> /* <-- remove scoped here if you have it*/
   .v-carousel__controls__item{
      color: #FF1744 !important
   }
</style>
