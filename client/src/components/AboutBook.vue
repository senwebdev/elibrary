<template>
<v-layout row wrap>
  <navbar></navbar>

  <div class="container section">
    <br/><br/>
    <v-subheader>What is this book about?</v-subheader>

    <div class="columns" >
      <div class="column is-8">
        <b-container class="">
          <b-row align-v="center">
            <b-col >
              <v-img :src="require(`@/assets/${book.img}`)" alt="published books" aspect-ratio="1" max-height="300px" max-width="300px"/>
            </b-col>
            <b-col >
              <v-flex>
                <h3>Title</h3>
                <v-label>{{book.title}}</v-label>
              </v-flex>
              <v-flex>
                <h3>Author</h3>
                <v-label>{{book.author}}</v-label>
              </v-flex>
            </b-col>
            <b-col >
              <v-btn outline large color="green"> 
                PLACE HOLD +
              </v-btn>
            </b-col>
          </b-row>
        </b-container>
      </div>

      <v-subheader>More details...</v-subheader>
      <v-divider></v-divider>

      <div class="column is-8">
        <b-container class="">
          <b-row >
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title >Title</v-list-tile-title>
                <v-list-tile-sub-title>{{book.title}}</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title >Author</v-list-tile-title>
                <v-list-tile-sub-title>{{book.author}}</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title >Publisher</v-list-tile-title>
                <v-list-tile-sub-title>{{book.publisher}}</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title >Distributor</v-list-tile-title>
                <v-list-tile-sub-title>{{book.distributor}}</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title >Description</v-list-tile-title>
                <v-list-tile-sub-title>{{book.description}}</v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-flex>
              <v-label >Note</v-label>
              <v-card v-for="(note, index) in book.notes" :key="index">
                <v-label>{{note.user}} : "{{note.note}}"</v-label>
              </v-card>
            </v-flex>
          </b-row>
        </b-container>
      </div>

      <v-divider></v-divider>
      <footer-bar />
    </div>
  </div>
</v-layout>
</template>

<script>
import axios from 'axios';
import EventBus from './EventBus'
import FooterBar from '@/components/FooterBar';
import NavBar from './NavBar'

export default {
  data: function(){
    return{
      book: []
    }
  },
  methods:{
    getbook() {
      const path = `http://localhost:5000/search?search_key=${this.$route.query.book_id}`;
      axios.get(path)
      .then((res) => {
        this.book = res.data[0];
        console.log(this.book)
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
    }
  },
  components:{
    FooterBar,
    navbar: NavBar
  },
  created(){
    this.getbook();
  },
}
</script>

<style>
#navbar{
  margin-top:0px;
}
</style>
