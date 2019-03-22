<template>
    <v-layout row wrap>
        <search class="search_form"></search>
        <v-label v-if="authorized">Please login to read full story...</v-label>
        <latestbooks></latestbooks>
        <popularbooks></popularbooks>
    </v-layout>
</template>

<script>
import LatestBooks from './LatestBooks'
import PopularBooks from './PopularBooks'
import Search from './Searchfield' 

export default {
    data: function(){
        return{
            authorized:''
        }
    },
    components: {
        'latestbooks': LatestBooks,
        'popularbooks': PopularBooks,
        'search': Search,
    }
}; 
</script>

<style>
.search_form{
    margin-left:75%;
    height:96px;
} 
</style>