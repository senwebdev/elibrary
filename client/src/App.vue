

<template>
  <div id="app">
    <div id="nav_bar" class="btn-group btn-group-toggle" data-toggle="buttons">
      <label class="btn btn-secondary active">
        <input type="radio" name="options" id="option1" autocomplete="off" checked><router-link to="/">Home</router-link>
      </label>
      <label v-if="isAuthenticated" class="btn btn-secondary">
        <input type="radio" name="options" id="option2" autocomplete="off"> <router-link to="/books">Books</router-link>
      </label>
      <label v-if="isAuthenticated" class="btn btn-secondary">
        <input type="radio" name="options" id="option2" autocomplete="off"> <router-link to="/profile">Profile</router-link>
      </label>
      <label v-if="!isAuthenticated" class="btn btn-secondary">
        <input type="radio" name="options" id="option3" autocomplete="off"> <router-link to="/login">Login</router-link>
      </label>
      <label v-if="isAuthenticated" class="btn btn-secondary">
        <input type="radio" name="options" id="option4" autocomplete="off"> <router-link to="/search">Search</router-link>
      </label>
      <label v-if="isAuthenticated" class="btn btn-secondary">
        <input type="radio" name="options" id="option5" autocomplete="off"> <router-link to="/logout">Logout</router-link>
      </label>
    </div>
    
    <router-view></router-view>
    
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      isAuthenticated: false
    };
  },
  async created() {
    try {
      await this.$auth.renewTokens();
    } catch (e) {
      console.log(e);
    }
  },
  methods: {
    login() {
      this.$auth.login();
    },
    logout() {
      this.$auth.logOut();
    },
    handleLoginEvent(data) {
      this.isAuthenticated = data.loggedIn;
      this.profile = data.profile;
    }
  }
};
</script>


<style>
#app {
  margin-top: 60px;
}
a, a:hover{
  color:white;
  text-decoration: none;
}
#nav_bar{
  margin-left:150px;
  margin-bottom:30px;
}
</style>