<template>
    <div class="row">
        <div class="">
            <form @submit.prevent="getBooks()">
                <input v-model="search_key" type="text" placeholder="Search for book"/>
                <v-btn type="submit">Search</v-btn>
            </form>        
        </div>
        <div>
          <h3 v-if="any_response" class="text-center">
            No search results!
          </h3>
        </div>
    </div>
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