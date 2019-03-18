<template>
  <v-app dark color="backcolor">
    <navbar></navbar>
    <router-view />
  </v-app>
</template>

<script>
import NavBar from './components/NavBar'

export default {
  name: 'App',
  components: {
    'navbar': NavBar
  },
  data () {
    return {
      //
    }
  }
}
</script>

<style>

</style>
