<template>
    <div id="nav_bar" class="btn-group btn-group-toggle" data-toggle="buttons">
        <label class="btn btn-secondary active">
        <input type="radio" name="options" id="option1" autocomplete="off" checked><router-link to="/">Home</router-link>
        </label>
        <label v-if="auth=='loggedin'" class="btn btn-secondary">
        <input type="radio" name="options" id="option2" autocomplete="off"> <router-link to="/books">Books</router-link>
        </label>
        <label v-if="auth=='loggedin'" class="btn btn-secondary">
        <input type="radio" name="options" id="option2" autocomplete="off"> <router-link to="/profile">Profile</router-link>
        </label>
        <label v-if="auth==''" class="btn btn-secondary">
        <input type="radio" name="options" id="option3" autocomplete="off"> <router-link to="/login">Login</router-link>
        </label>
        <label v-if="auth=='loggedin'" class="btn btn-secondary">
        <input type="radio" name="options" id="option4" autocomplete="off"> <router-link to="/search">Search</router-link>
        </label>
        <label v-if="auth=='loggedin'" class="btn btn-secondary">
        <input type="radio" name="options" id="option5" autocomplete="off"> <a href="" class="nav_link" v-on:click="logout">Logout</a>
        </label>
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
