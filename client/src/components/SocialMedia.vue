<template>

  <v-footer
    dark
    height="auto"
    fixed
  ><i class="fa fa-github" aria-hidden="true"></i>
<i class="fa fa-github"></i>

    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title>
        <strong class="subheading">Get connected with us on social networks!</strong>
        <v-spacer></v-spacer>
        <v-btn
          v-for="(icon, index) in icons"
          :key="index"
          class="mx-3"
          dark
          icon
        >
          <a :href="icon.url" :target="icon.target"><v-icon size="24px">{{ icon.name }}</v-icon></a>
        </v-btn>
      </v-card-title>
      <v-card-actions class="grey darken-3 justify-center">
        &copy;2018 — <strong>Vuetify</strong>
      </v-card-actions>
    </v-card></v-footer>
</template>

<script>
 export default {
    data: () => ({
      icons: [
        {
            name:'fab fa-twitter',
            url: 'https://www.twitter.com/',
            target: '_blank'
        },
        {
            name:'fab fa-github',
            url: 'https://www.github.com/AfricanTurtles',
            target: '_blank'
        },
        {
            name:'fab fa-linkedin',
            url: 'https://www.linkedin.com/in/AfricanTurtles',
            target: '_blank'
        },
        {
            name:'fab fa-instagram',
            url: 'https://www.instagram.com/AfricanTurtles',
            target: '_blank'
        }
      ]
    })
  }

</script>