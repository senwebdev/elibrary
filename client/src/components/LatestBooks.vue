<template>

  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-btn class="white--text" id="watch-btn" color="green accent-4">Latest Books</v-btn>
    </v-layout>
    <v-layout row wrap>
      <v-flex v-for="(book, index) in books" :key="index" sm>
        <v-card dark color="primary" oncontextmenu="return false" @mouseleave="leaveFlex(index, $event)" >
          <v-img class="image" :src="require(`@/assets/${book.img}`)" alt="published books" aspect-ratio="1" @mouseover="showSummary(index, $event)"/>
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
  </v-container> 
</template>
 
<script>
import axios from 'axios';
import EventBus from './EventBus'
import Router from '../router';

export default {
  data () {
    return{
      books: [],
      isHovers: [],
      auth: '',
    }
  },
  methods: {
    getLatestBooks() { 
      const path = 'https://elibraryserver.herokuapp.com/latest_books';
      axios.get(path)
      .then((res) => {
        this.books = res.data;
        for (let i = 0; i < this.books.length; i++) {
          this.isHovers[i] = false;
        }
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
    aboutBooks: function(bookid){
      Router.push({ path: 'aboutbook', query: {book_id: bookid}})
    }
  },
  created(){
    this.getLatestBooks();
  },
  mounted () {
    this.auth = localStorage.loggedIn;
  }
}

</script>

<style>

.image:hover {
 opacity: 0.5;
}

.row{
  padding:20px;
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

#watch-btn, #watch-btn:disabled{
  background:green;
}

</style>