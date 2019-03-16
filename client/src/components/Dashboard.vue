<template>
    <div class="container">
        <search class="search_form"></search>
        <latestbooks></latestbooks>
    </div>
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
    position:fixed;
    left:80%;
    width:300px;
    position: fixed;
    left: 75%;
    width: 360px;
} 
</style>