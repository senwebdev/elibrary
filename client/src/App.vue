<template>
  <v-app dark color="backcolor">
    <router-view />
  </v-app>
</template>

<script>
export default {
  name: 'App',
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
