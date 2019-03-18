<template>
    <v-layout>
        <search class="search_form"></search>
        <latestbooks></latestbooks>
    </v-layout>
</template>

<script>
import LatestBooks from './LatestBooks'
import Search from './Searchfield' 

export default {
    components: {
        'latestbooks': LatestBooks,
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