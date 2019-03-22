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
*, *::before, *::after {
	box-sizing: border-box;
}

body {
	padding: 0;
	margin: 0;
	font-family: 'PT Sans', sans-serif;
	background:#e0e0e0;
}
</style>
