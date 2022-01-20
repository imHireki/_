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
         <router-link
           to="/"
           style="text-decoration: none; color: inherit;"
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
          </router-link>
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

                <button slot="append">
                  <v-icon
                    color="red accent-3"
                  >
                    mdi-magnify
                  </v-icon>
                </button>

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
        <v-row>
          <v-col cols="8">
            <div class="upload-example">

              <cropper
                ref="cropper"
                class="upload-example-cropper"
                :src="image.src"
              />

              <div class="button-wrapper">
                <input type="file" ref="file" @change="loadImage($event)" accept="image/*">
                <v-btn @click.stop="crop()">Crop</v-btn>
                <v-btn @click.stop="reset()">Reset</v-btn>
              </div>

            </div>

          </v-col>
        </v-row>

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
  import axios from 'axios';
  import { Cropper } from 'vue-advanced-cropper';
  import 'vue-advanced-cropper/dist/style.css';

  // This function is used to detect the actual image type,
  function getMimeType(file, fallback = null) {
    const byteArray = (new Uint8Array(file)).subarray(0, 4);
      let header = '';
      for (let i = 0; i < byteArray.length; i++) {
        header += byteArray[i].toString(16);
      }
    switch (header) {
          case "89504e47":
              return ["image/png", "png"];
          case "47494638":
              return ["image/gif", "gif"];
          case "ffd8ffe0":
          case "ffd8ffe1":
          case "ffd8ffe2":
          case "ffd8ffe3":
          case "ffd8ffe8":
              return ["image/jpeg", "jpg"];
          default:
              return fallback;
      }
  }

  export default {
    name: 'App',

    components: {
      Cropper,
    },

    data() {
      return {
        image: {
          src: null,
          type: null,
          ext: null,
        },
        drawer: true,
      };
    },

    methods: {
      crop() {
        const { canvas } = this.$refs.cropper.getResult();

        if (canvas) {
          const data = new FormData();

          canvas.toBlob((blob) => {
            console.log(blob)
            data.append('image', blob, `blob.${this.image.ext}`);
            axios
              .put('http://127.0.0.1:8000/api/v1/icons/upload/',
                   data)
              .then(response => {
                console.log(response)
              });
          }, this.image.type);

        }
      },

      reset() {
        this.image = {
          src: null,
          type: null
        }
      },

      loadImage(event) {
        // Reference to the DOM input element
        const { files } = event.target;
        // Ensure that you have a file before attempting to read it
        if (files && files[0]) {
          // 1. Revoke the object URL, to allow the garbage collector to destroy the uploaded before file
          if (this.image.src) {
            URL.revokeObjectURL(this.image.src)
          }
          // 2. Create the blob link to the file to optimize performance:
          const blob = URL.createObjectURL(files[0]);

          // Create a new FileReader to read this image binary data
          const reader = new FileReader();
          // Define a callback function to run, when FileReader finishes its job
          reader.onload = (e) => {
            let mime = getMimeType(e.target.result, files[0].type[0])
            // Note: arrow function used here, so that "this.image" refers to the image of Vue component
            this.image = {
              // Set the image source (it will look like blob:http://example.com/2c5270a5-18b5-406e-a4fb-07427f5e7b94)
              src: blob,
              // Determine the image type to preserve it during the extracting the image from canvas:
              type: mime[0],
              ext: mime[1],
            };
          };
          // Start the reader job - read file as a data url (base64 format)
          reader.readAsArrayBuffer(files[0]);
        }
      },
    },
    destroyed() {
      // Revoke the object URL, to allow the garbage collector to destroy the uploaded before file
      if (this.image.src) {
        URL.revokeObjectURL(this.image.src)
      }
    }
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
