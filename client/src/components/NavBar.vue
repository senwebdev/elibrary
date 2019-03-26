<template>
    <div id="nav_bar">
      <!-- User Not Authorized -->
      <v-toolbar v-if="auth==''" dark color="secondary" class="toolbar">
        
        <v-toolbar-title class="white--text">eLibrary</v-toolbar-title>
        <v-spacer></v-spacer>
        <router-link to="/">
          <v-btn round icon>
            <v-icon>home</v-icon>
          </v-btn>
        </router-link>
        <router-link to="/login">
          <v-btn round icon>
            <v-icon>account_circle</v-icon>
          </v-btn>
        </router-link>
      </v-toolbar>

      <!-- User Authorized -->
      <v-toolbar v-if="auth=='loggedin'" dark color="secondary">
        <v-toolbar-title class="white--text">eLibrary</v-toolbar-title>
        <v-spacer></v-spacer>
        <router-link to="/">
          <v-btn round icon>
            <v-icon>home</v-icon>
          </v-btn>
        </router-link>
        <router-link to="/books">
          <v-btn round icon>
            <v-icon>library_books</v-icon>
          </v-btn>
        </router-link>
        <router-link to="/profile">
          <v-btn round icon>
            <v-icon>account_box</v-icon>
          </v-btn>
        </router-link>          
        <a href="/" v-on:click="logout">
          <v-btn round icon>
            <v-icon>exit_to_app</v-icon>
          </v-btn>
        </a>
      </v-toolbar>
    </div>
</template>

<script>
import EventBus from './EventBus'

EventBus.$on('logged-in', test => {
  console.log(test)
})
export default {
  data () {
    return {
      auth: '',
      user: ''
    }
  },

  components: {
  },

  methods: {
    logout () {
      localStorage.removeItem('usertoken')
    }
  },

  mounted () {
    EventBus.$on('logged-in', status => {
      this.auth = status
    })
  }

}
</script>

<style>
#nav_bar a{
  text-decoration: none
}
#nav_bar .toolbar{
  position:fixed;
  z-index:30;
}
</style>