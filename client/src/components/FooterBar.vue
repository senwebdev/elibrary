<template>
    <div class="columns" >
        <b-container class="">
          <b-row align-v="start">
            <b-col >
                <h3>Developer's</h3>
                <h3>Public</h3>
                <h3 style="font-weight:bold">eLibrary</h3>
                <br/><br/><br/><br/>
                <h5>© The Developer's Public Library, 2019</h5>
            </b-col>
            <b-col >
                <v-layout aign-center justify-space-around>
                    <v-label><router-link to="/">Home</router-link></v-label>
                    <v-label><router-link to="profile">About Us</router-link></v-label>
                    <v-label><router-link to="#">Subscribe</router-link></v-label>
                    <v-label><router-link to="#">History</router-link></v-label>
                    <v-label><router-link to="#">Developers</router-link></v-label>
                </v-layout>

                <v-layout>
                    <socialmedia></socialmedia>
                </v-layout>
            </b-col>
          </b-row>
        </b-container>
    </div>
</template>

<script>
import socialmedia from './SocialMedia'

export default{
    components:{
        socialmedia
    }
}
</script>
