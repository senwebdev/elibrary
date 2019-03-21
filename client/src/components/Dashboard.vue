<template>
    <v-layout>
        <search class="search_form"></search>
        <latestbooks></latestbooks>
        <popularbooks></popularbooks>
    </v-layout>
</template>

<script>
import LatestBooks from './LatestBooks'
import PopularBooks from './PopularBooks'
import Search from './Searchfield' 

export default {
    components: {
        'latestbooks': LatestBooks,
        'popularbooks': PopularBooks,
        'search': Search
    }
}; 
</script>

<style>
.search_form{
    position: fixed;
    left: 75%;
    width: 360px;
} 
</style>