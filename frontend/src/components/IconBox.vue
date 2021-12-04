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
      <v-carousel
        :hide-delimiter-background="true"
        :hide-delimiters="check_len_images(icon.images)"
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

      <v-card-title
        class="text-h5  text-truncate"
        style="max-width: 100%"
      >
        oi{{ icon.name }}
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
        return false
      } else {
        return true
      }
    } 
  },
}
</script>
