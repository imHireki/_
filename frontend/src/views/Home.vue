<template>
  <v-app id="inspire">
    
    <!-- APP BAR -->
    <v-app-bar
      app
      hide-on-scroll
      flat
      scroll-threshold="200"
    >
      <!-- TITLE -->
      <v-toolbar-title
        class="title mr-5">
        <v-btn
          class="ma-2"
          text
          icon
        >
          <v-icon
            color="red accent-3"
            x-large
          >mdi-wizard-hat
          </v-icon>
        </v-btn>

        Yamerooo
      </v-toolbar-title> 
      <!-- / TITLE -->

      <!-- SEARCH -->
      <v-text-field
        dense
        flat
        hide-details
        rounded
        solo-inverted
        placeholder="megumin"
        class="grey lighten-2"
      >
          <v-icon
            slot="append"
            color="red accent-3"
            @click.stop="drawer = !drawer"
          >
            mdi-magnify
          </v-icon> 

      </v-text-field>
      <!-- / SEARCH -->

    </v-app-bar>
    <!-- \ APP BAR -->

    <!-- DRAWER -->
    <v-navigation-drawer
      v-model="drawer"
      app
      width="300"
    >
      <v-navigation-drawer
        v-model="drawer"
        absolute
        color="grey lighten-3"
        mini-variant
      >
        <v-avatar
          class="d-block text-center mx-auto mt-4"
          color="grey darken-1"
          size="36"
        ></v-avatar>

        <v-divider class="mx-3 my-5"></v-divider>

        <v-avatar
          v-for="n in 6"
          :key="n"
          class="d-block text-center mx-auto mb-9"
          color="grey lighten-1"
          size="28"
        ></v-avatar>
      </v-navigation-drawer>

      <v-sheet
        color="grey lighten-5"
        height="128"
        width="100%"
      ></v-sheet>

      <v-list
        class="pl-14"
        shaped
      >
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-content>
            <v-list-item-title>Item {{ n }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <!-- \ DRAWER -->

    <!-- MAIN --> 
    <v-main class="pa-2">
      <v-row no-gutters>
        <v-col
          v-for="icon in icons"
          :key="icon.id"
          cols="6"
          md="3"
          lg="3"
          xl="2" 
        >
          <v-card
            class="pa-2 ma-1"
            shaped
            hover
          >
            <v-img
              class="rounded-circle"
              :style="{'background-color': icon.color}"
              alt=""
              :src="icon.get_small_image"
              :aspect-ratio="1/1"
              contain
            >
              <template v-slot:placeholder>
                <v-row
                  class="fill-height ma-0"
                  align="center"
                  justify="center"
                >
                  <v-progress-circular
                    indeterminate
                    color="red accent-3"
                  ></v-progress-circular>
                </v-row>
              </template> 

            </v-img>

            <v-card-title
              class="text-h5  text-truncate"
              style="max-width: 100%"
            >
              {{ icon.name }}
            </v-card-title>


            <v-card-actions>
              <v-list-item class="grow px-2">
                <v-list-item-avatar
                  :color="icon.color"
                >
                <!-- TODO: add avatar -->
                </v-list-item-avatar>

                <v-list-item-content>
                  <v-list-item-title>
                    {{ icon.user.username }}
                  </v-list-item-title>
                </v-list-item-content>

                <v-row
                  align="center"
                  justify="end"
                >
                  <v-icon class="mr-1" color="red accent-3">
                    mdi-heart
                  </v-icon>

                </v-row>

              </v-list-item>
            </v-card-actions>
          </v-card>

        </v-col>
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

    </v-main>
    <!-- \ MAIN -->

    <!-- FOOTER -->
    <v-footer
      app
      color="transparent"
      height="72"
      inset
    >
      <v-btn
        text
        icon
        class="mx-2"
        @click.stop="drawer = !drawer"
        color="red accent-3"
      >
        <v-icon
          large
        >
          mdi-forwardburger
        </v-icon>
      </v-btn>
    </v-footer>
    <!-- \ FOOTER -->

  </v-app>
</template>

<script>
  import axios from 'axios'

  export default {
      name: 'Home',
      data() {
          return {
              drawer: null,
              icons: [],
              page: 1,
              hasNextPage: true,
          }
      },
      methods: {
          async getIcons() {
              await axios
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
      },
  }
</script>
