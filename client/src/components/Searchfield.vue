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
                    <th scope="col">Read?</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(book, index) in books" :key="index">
                    <td>{{ book.title }}</td>
                    <td>{{ book.author }}</td>
                    <td>
                        <span v-if="book.read">Yes</span>
                        <span v-else>No</span>
                    </td>                
                </tr>
            </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
        books: [],
        search_key:''
    }
  },

  methods: {
    getBooks() {
      const path = `http://localhost:5000/search?search_key=${this.search_key}`;
      axios.get(path)
      .then((res) => {
        this.books = res.data;
        console.log(this.search_key)
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
    },
  }
}
</script>