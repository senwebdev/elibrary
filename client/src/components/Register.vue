<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 mt-5 mx-auto">
        <form v-on:submit.prevent="register">
          <h1 class="h3 mb-3 font-weight-normal">Register</h1>
          <div class="form-group">
            <label for="name">First name</label>
            <input type="text" v-model="firstname" class="form-control" name="first_name" placeholder="Enter your first name">
          </div>
          <div class="form-group">
            <label for="name">Last name</label>
            <input type="text" v-model="lastname" class="form-control" name="last_name" placeholder="Enter your lastname name">
          </div>
          <div class="form-group">
            <label for="email">Email address</label>
            <input type="email" v-model="email" class="form-control" name="email" placeholder="Enter email">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" v-model="password" class="form-control" name="password" placeholder="Password">
          </div>
          <div class="form-group">
            <label for="passwordcheck">Confirm Password</label>
            <input class="form-control" required type="password" v-model='passwordChck' placeholder="Check your password confirmation">
          </div>

          <button type="submit"  class="btn btn-lg btn-primary btn-block">Register!</button>
          <v-card style="margin:20px">Log in with existing account? Click <a href="login" style="text-decoration:underline">here</a> to visit SignIn Page.</v-card>
        </form>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import router from '../router'

const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

export default {
  data () {
    return {
      firstname: '',
      lastname: '',
      email: '',
      password: '',
      passwordChck: ''
    }
  },
  computed: {
    isFormValid () {
      return (
          this.isValid('firstname') && 
          this.isValid('lastname') && 
          this.isValid('email') && 
          this.isValid('password') && 
          this.isValid('passwordChck')
      )
    }
  },
  methods: {
    isValid(prop) {
      switch (prop) {
        case 'firstname':
            return this.firstname.length >= 2
            break
        case 'lastname':
            return this.lastname.length >= 2
            break
        case 'email':
            return emailRegex.test(this.email)
            break
        case 'password':
            return this.password.length >= 6
            break
        case "passwordChck":
            return this.password === this.passwordChck
            break
        default:
            return false
      }
    },
    resetUser () {
        this.firstname = ''
        this.lastname = ''
        this.email = ''
        this.password = ''
        this.passwordChck = ''
    },
    register () {
      axios.post('https://elibraryserver.herokuapp.com/users/register',
        {
          first_name: this.firstname,
          last_name: this.lastname,
          email: this.email,
          password: this.password
        }
      ).then((res) => {
        console.log(res)
        router.push({ name: 'Login' })
      }).catch((err) => {
        console.log(err)
      })
    }
  },
}
</script>
