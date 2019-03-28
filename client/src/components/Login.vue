<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3 mx-auto my-auto">
        <form v-on:submit.prevent="login">
          <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
          <div class="form-group">
            <label for="email">Email address</label>
            <input type="email" v-model="email" class="form-control" name="email" placeholder="Enter email">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" v-model="password" class="form-control" name="password" placeholder="Password">
          </div>
          <button type="submit" :disabled='!isFormValid' class="btn btn-lg btn-primary btn-block">Sign in</button>
        </form>
        <v-card style="margin:10px">Don't you have your account? Click <a href="register" style="text-decoration:underline">here</a> to visit SignUp Page.</v-card>
      </div>
    </div>
    

    <v-alert
        :value="true"
        type="error"
        v-if="confirmation == 'invalid'"
        class="alert"
      >
        This username or password is invalid!
      </v-alert>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'
import EventBus from './EventBus'
const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

export default {
  data () {
    return {
      email: '',
      password: '',
      confirmation: ''
    }
  },
  computed: {
    isFormValid () {
      return (
          this.isValid('email') && 
          this.isValid('password')
      )
    }
  },
  methods: {
    isValid(prop) {
      switch (prop) {
        case 'email':
            return emailRegex.test(this.email)
            break
        case 'password':
            return this.password.length >= 6
            break
        default:
            return false

      }
    },
    resetFormValues () {
        this.user.email = ''
        this.user.password = ''
    },
    login () {
      axios.post('https://elibraryserver.herokuapp.com/users/login',
        {
          email: this.email,
          password: this.password
        }
      ).then((res) => {
        if(res.data.error) {
          this.confirmation = 'invalid'
        } else{
          localStorage.setItem('usertoken', res.data)
          router.push('/')
        }
      }).catch((err) => {
        console.log(err)
      })
      this.emitMethod()
    },
    emitMethod () {
      EventBus.$emit('logged-in', 'loggedin')
    }
  }
}
</script>

<style>
.alert{
  width:500px;
}
</style>