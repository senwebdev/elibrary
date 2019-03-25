<template>
    <v-layout class="row">
        <v-card >
          <v-text-field
            @keyup.enter="getBooks()"
            box
            label="Search for the books"
            append-icon="search"
            v-model = "search_key"
          >
          </v-text-field>
        </v-card>
    </v-layout>
</template>

<script>
import Router from '../router';
export default {
  data() {
    return {
        search_key:'',
    }
  },
  methods: {
    getBooks() {
      Router.push({ path: 'search', query: {search_key: this.search_key}})
    },
  }
}
</script>

<style>

</style>