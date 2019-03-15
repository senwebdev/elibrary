<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <navbar></navbar>
    <router-view />
  </div>
</template>

<script>
import NavBar from './components/NavBar'

export default {
  name: 'App',
  components: {
    'navbar': NavBar
  }
}
</script>
