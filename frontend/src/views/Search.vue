<template>
  <div class="search-page">
    <span>
      <p class="subtitle text-center">Searching for: <b>{{ query }}</b></p>
    </span>
    <v-row>
      <IconBox v-for="icon in icons" :key="icon.id" :icon="icon"/>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios'
import IconBox from '../components/IconBox.vue'

export default  {
  name: 'Search',
  data() {
    return {
      query: '',
      icons: [],
      page: 1,
      hasNextPage: false,
    }
  },
  components: {
    IconBox
  },
  mounted() {
    let uri = window.location.search.substring(1)
    let params = new URLSearchParams(uri)

    if (params.get('query')) {
      this.query = params.get('query')
      this.getIcons()
      this.getNextPage()
    }
  },
  methods: {
    getIcons() {
      axios
        .post(`http://127.0.0.1:8000/api/v1/icons/search/?page=${this.page}`,
              {'query': this.query})
        .then(response => {
          for (let i = 0; i < response.data.results.length; i++) {
            this.icons.push(response.data.results[i])
          }
          if (response.data.next) {
             this.hasNextPage = true
          } else {
             this.hasNextPage = false
          }
        })
    },
    getNextPage() {
      window.onscroll = () => {
        let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
        if (bottomOfWindow && this.hasNextPage) {
          this.page += 1
          this.getIcons()
        }
      }
    }
  }
}
</script>

