<template>
    <div>
        <div class="col-md-3">
            <form @submit.prevent="getBooks()">
                <input v-model="search_key" type="text" placeholder="Search for book"/>
                <button type="submit">Search</button>
            </form>        
        </div>
        <div>
            <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Author</th>
                    <th scope="col">Available</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(book, index) in books" :key="index">
                    <td>{{ book.title }}</td>
                    <td>{{ book.author }}</td>
                    <td>
                        <span v-if="book.available">Yes</span>
                        <span v-else>No</span>
                    </td>                
                </tr>
            </tbody>
            </table>
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