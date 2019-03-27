<template>
    <div id="nav_bar">
      <!-- User Not Authorized -->
      <v-toolbar v-if="isAuthorized()==false" dark color="secondary" class="toolbar">
        
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
      <v-toolbar v-if="isAuthorized()==true" dark color="secondary" class="toolbar">
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
export default {
  data () {
    return {
      isLoggedin: '',
    }
  },

  methods: {
    isAuthorized: function(){
      var isLoggedin = localStorage.getItem('usertoken')
      return isLoggedin ? true : false;
    },
    logout () {
      localStorage.removeItem('usertoken')
    }
  },
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
#nav_bar{
  margin-top:-20px
}
</style>