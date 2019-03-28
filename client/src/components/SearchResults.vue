<template>
<v-layout row wrap>
  <navbar></navbar>
  <v-container grid-list-md>
    <br/>
    <search class="search_form"></search>
    <v-layout row wrap>
      <v-btn v-if="any_response" class="white--text" id="watch-btn" color="green accent-4">Search Results</v-btn>
      <v-btn v-else class="white--text" id="watch-btn" color="green accent-4">No Results</v-btn>
    </v-layout>
    <v-layout row wrap>
      <v-flex class="card" v-for="(book, index) in books" :key="index" xs2>
        <v-card dark color="primary" oncontextmenu="return false" @mouseleave="leaveFlex(index, $event)" >
          <v-img class="image" :src="`${book.img}`" alt="published books" aspect-ratio="1" @mouseover="showSummary(index, $event)"/>
          <!-- <transition name="fade" > -->
            <v-flex class="summary" v-if="isHovers[index]" >
              <v-card-text> Title : {{book.title}} </v-card-text>
              <v-card-text> Author : {{book.author}} </v-card-text>
              <v-card-text> Available : {{book.available}} </v-card-text>
              <v-btn v-bind:disabled="isAuthorized()" v-on:click="aboutBooks(book._id)" color="green accent-4">GO</v-btn>
            </v-flex>
          <!-- </transition> -->
        </v-card>
      </v-flex>
    </v-layout>
    <v-divider></v-divider>
    <footer-bar />

  </v-container> 
</v-layout>
</template>
 
<script>
import axios from 'axios';
import EventBus from './EventBus'
import Router from '../router'
import FooterBar from '@/components/FooterBar';
import search from './Searchfield';
import NavBar from './NavBar'

export default {
  data () {
    return{
      books: [],
      isHovers: [],
      auth: '',
      search_key:'',
      any_response: false
    }
  },
  components:{
    search,
    FooterBar,
    'navbar': NavBar
  },
  methods: {
    getBooks(){
      const path = `https://elibraryserver.herokuapp.com/search?search_key=${this.$route.query.search_key}`;
      axios.get(path)
      .then((res) => {
        this.any_response = (res.data.length > 0) ? true : false
        console.log(this.any_response, "search results")
        this.books = res.data
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
    },
    showSummary: function(index, event) {
      if(event.target.className == "v-responsive__content" || event.target.className == "v-responsive v-image image")
        this.isHovers[index] = true;
      this.isHovers = this.isHovers.slice();
    },
    leaveFlex: function(index, event){
      if(event.target.className == "v-card v-sheet theme--dark primary")
        this.isHovers[index] = false;
      this.isHovers = this.isHovers.slice();
    },
    isAuthorized: function(){
      var isLoggedin = localStorage.getItem('usertoken')
      return isLoggedin ? false : true;
    },
    aboutBooks(bookid){
      Router.replace({ path: 'aboutbook', query: {book_id: bookid}})
    }
  },
  created(){
    this.getBooks();
  },
  mounted () {
    this.auth = localStorage.loggedIn;
  },
  watch:{
    '$route' (to, from){
      this.$router.go(0);
    }
  }
}

</script>

<style scoped>

.image:hover {
 opacity: 0.5;
}

.row{
  padding:20px;
}
.search_form{
    margin-left:75%;
    margin-top:3%;
    height:96px;
} 
.summary{
  width:300px;
  z-index: 10;
  margin-top: -70px;
  margin-left: 150px;
  position: absolute;
  color: black;
  background: white;
  opacity: 0.9;
  border-top-left-radius:10px;
}
.summary a{
    text-decoration: none
}

#watch-btn, #watch-btn:disabled{
  background:green;
}

</style>