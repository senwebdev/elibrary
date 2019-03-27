<template>
    <v-layout row wrap>
        <navbar></navbar>
        <search class="search_form"></search>
        <v-label v-if="isAuthorized()">Please login to read full story...</v-label>
        <latestbooks></latestbooks>
        <popularbooks></popularbooks>
    </v-layout>
</template>

<script>
import LatestBooks from './LatestBooks'
import PopularBooks from './PopularBooks'
import Search from './Searchfield' 
import Router from '../router'
import NavBar from './NavBar'

export default {
    methods:{
        isAuthorized: function(){
        var isLoggedin = window.localStorage.getItem('usertoken')
        return isLoggedin ? false : true;
        }
    },
    components: {
        'latestbooks': LatestBooks,
        'popularbooks': PopularBooks,
        'search': Search,
        'navbar': NavBar
    }
}
</script>

<style>
.search_form{
    margin-left:75%;
    margin-top:3%;
    height:96px;
} 
</style>