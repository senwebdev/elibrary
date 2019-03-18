<template>
    <div id="nav_bar">
        <v-toolbar dark color="secondary">
          <v-toolbar-side-icon></v-toolbar-side-icon>
          <v-toolbar-title class="white--text">eLibrary</v-toolbar-title>
          <v-spacer></v-spacer>
            <router-link to="/">
              <v-btn round icon>
                <v-icon>home</v-icon>
              </v-btn>
            </router-link>
            <router-link v-if="auth=='loggedin'" to="/books">
              <v-btn round icon>
                <v-icon>library_books</v-icon>
              </v-btn>
            </router-link>
            <router-link v-if="auth=='loggedin'" to="/profile">
              <v-btn round icon>
                <v-icon>account_box</v-icon>
              </v-btn>
            </router-link>          
            <router-link v-if="auth==''" to="/login">
              <v-btn round icon>
                <v-icon>account_circle</v-icon>
              </v-btn>
            </router-link>
            
            <a v-if="auth=='loggedin'" href="/" v-on:click="logout">
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
