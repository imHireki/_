<template>
  <v-app id="inspire">
    
    <!-- APP BAR -->
    <v-app-bar
      app
      clipped-right
      flat
      height="72"
    >
      <v-spacer></v-spacer>

      <v-responsive max-width="156">
        <v-text-field
          dense
          flat
          hide-details
          rounded
          solo-inverted
        ></v-text-field>
      </v-responsive>

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
        md="4"
        lg="3"
        xl="2" 
      >
        <v-card
          class="pa-2"
          outlined
          tile
        >
          <v-card-title>
            <v-img
              class="elevation-6 rounded-circle"
              alt=""
              :src="icon.get_image"
              :aspect-ratio="1/1"
              contain
            ></v-img>
          </v-card-title>

          <v-card-text
            class="text-h5 font-weight-bold text-truncate"
            style="max-width: 99%"
          >
            {{ icon.name }}
          </v-card-text>

          <v-card-actions>
            <v-list-item class="grow">
              <v-list-item-avatar color="grey darken-3">
                <v-img
                  class="elevation-6"
                  alt=""
                  src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                ></v-img>
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title>{{ icon.user.username }}</v-list-item-title>
              </v-list-item-content>

              <v-row
                align="center"
                justify="end"
              >
                <v-icon class="mr-1" color="red">
                  mdi-heart
                </v-icon>
                <span class="subheading mr-2">256</span>

                <span class="mr-1">·</span>

                <v-icon class="mr-1" color="blue">
                  mdi-share-variant
                </v-icon>

                <span class="subheading">45</span>
              </v-row>

            </v-list-item>
          </v-card-actions>

        </v-card>

      </v-col>

    </v-row>


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
      >
        <v-icon
          large
          color="primary">mdi-forwardburger</v-icon>
      </v-btn>

      <v-text-field
        background-color="grey lighten-1"
        dense
        flat
        hide-details
        rounded
        solo
      ></v-text-field>

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
              icons: []
          }
      },
      created() {
          axios
          .get('http://127.0.0.1:8000/api/v1/icons/') 
          .then(response => {
              this.icons = response.data.results
          })
          .catch(error => {
              console.log(error)
          })
      }
  }
</script>
