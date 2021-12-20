<template>
  <v-app>
    <v-main>
      <!-- APP BAR -->
      <v-app-bar
        app
        hide-on-scroll
        flat
        scroll-threshold="200"
      >
        <!-- TITLE -->
        <v-toolbar-title
          class="title mr-5"
        >
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
        <v-row>
          <v-col>

            <v-form method="get" action="/search">
              <v-text-field
                dense
                flat
                hide-details
                rounded
                solo-inverted
                placeholder="megumin"
                class="grey lighten-2"
                name="query"
              >
                <v-icon
                  slot="append"
                  color="red accent-3"
                  @click.stop="drawer = !drawer"
                >
                  mdi-magnify
                </v-icon> 
              </v-text-field>
            </v-form>

          </v-col>
        </v-row>
        <!-- / SEARCH -->

      </v-app-bar>
      <!-- \ APP BAR -->

      <!-- DRAWER -->
      <v-navigation-drawer
        v-model="drawer"
        app
        width="300"
        height="100%"
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
        <router-view/>
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
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    drawer: null
  }),
};
</script>

<style>
  .v-carousel__controls__item{
    color: #FF1744 !important
  }
 .v-overlay__scrim{
    opacity: 0 !important
 }
</style>
