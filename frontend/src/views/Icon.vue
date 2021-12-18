<template>
  <div id="page-icon">
    {{ icon  }}
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
        }
    }

}
</script>
