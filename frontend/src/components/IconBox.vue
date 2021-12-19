<template>
  <v-col
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
      <template v-if="check_len_images(icon.images)">
        <v-carousel
          :hide-delimiter-background="true"
          :show-arrows="false"
          height="auto"
        >
          <v-carousel-item
            v-for="image in icon.images"
            :key="image.id"
          >

            <v-img
              class="rounded-circle"
              :style="{'background-color': image.color}"
              alt=""
              :src="image.get_image_256x"
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

          </v-carousel-item>
        </v-carousel>
      </template>

      <template v-else>
        <v-img
          class="rounded-circle"
          :style="{'background-color': image.color}"
          alt=""
          v-for="image in icon.images"
          :key="image.id"
          :src="image.get_image_256x"
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
      </template>

      <v-card-title
        class="text-h5  text-truncate px-0 py-1"
        style="max-width: 100%"
      >
        <router-link style="text-decoration: none; color: inherit;"
          :to="icon.get_icon_url"
        >
          {{ icon.name }}
        </router-link>
      </v-card-title>

      <v-card-actions>
        <v-list-item class="grow pa-0">

          <v-list-item-avatar
            color="grey darken-3"
            v-for="image in icon.images.slice(0, 1)"
            :key="image.id"
          >
            <v-img
              class="rounded-circle"
              :src="image.get_image_256x"
            >
            </v-img>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>{{ icon.user.username }}</v-list-item-title>
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
</template>

<script>
export default {
  name: 'IconBox',
  props: {
    icon: Object
  },
  methods: {
    check_len_images(images) {
      if(images.length > 1) {
        return true
      } else {
        return false
      }
    } 
  },
}
</script>
