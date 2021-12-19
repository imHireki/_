<template>
  <div id="page-icon">

    <v-row>
      <v-col>
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
      </v-col>

      <v-col>
        <p class="body-1">{{ icon.name }}</p>
        <p class="body-1">description</p>
        <p class="body-1">hashtags | tags</p>

        <span>
          <p class="d-inline">from: </p>
          <v-avatar
            class="d-inline"
            v-for="image in icon.images.slice(0, 1)"
            :key="image.id"
          >
            <v-img
            :src="image.get_image_256x"
            >
            </v-img>
          </v-avatar>

          <p class="d-inline">{{ icon.user.username }}</p>
        </span>

        <div>
          128<v-icon color="red accent-3">mdi-heart</v-icon>
          256<v-icon color="blue accent-3">mdi-tray-arrow-down</v-icon>
        </div>
      </v-col>

    </v-row>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Icon',
  data() {
    return {
      icon: {}
    }
  },
  mounted() {
    this.getIcon()
  },
  methods: {
    getIcon() {
      const slug = this.$route.params.slug

        axios
          .get(`http://127.0.0.1:8000/api/v1/icons/${slug}`)
          .then(response => {
             this.icon = response.data
          })
        },
    check_len_images(images) {
      if(images.length > 1) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>
