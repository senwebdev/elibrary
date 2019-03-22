<template>
    <v-layout class="row">
        <v-card >
            
            <v-text-field
              @keyup.enter="getBooks()"
              box
              label="Search for the books"
              append-icon="search"
            >
            </v-text-field>
          
        </v-card>
        <v-label>
          <h3 v-if="any_response" class="">
            No search results!
          </h3>
        </v-label>
    </v-layout>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
        books: [],
        search_key:'',
        any_response: false, 
    }
  },

  methods: {
    getBooks() {
      this.any_response = false
      const path = `http://localhost:5000/search?search_key=${this.search_key}`;
      axios.get(path)
      .then((res) => {
        this.any_response = (res.data.length > 0) ? false : true
        console.log(res.data)
        this.books = res.data; 
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
    },
  }
}
</script>

<style>

</style>