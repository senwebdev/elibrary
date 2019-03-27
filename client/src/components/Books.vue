
<template>
<v-layout row wrap>
  <navbar></navbar>
  <div class="container" id="books">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>

        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Book</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Avilable</th>
              <th></th>
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
              <td>
                <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.book-update-modal
                  @click="editBook(book)">
                  Update
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteBook(book)">
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addBookModal"
             id="book-modal"
             title="Add a new book"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addBookForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.available" id="form-checks">
            <b-form-checkbox value="true">Available</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editBookModal"
            id="book-update-modal"
            title="Update"
            hide-footer>
    <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
        <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
        </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                    label="Author:"
                    label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                        type="text"
                        v-model="editForm.author"
                        required
                        placeholder="Enter author">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-edit-group">
        <b-form-checkbox-group v-model="editForm.available" id="form-checks">
            <b-form-checkbox value="true">Avilable</b-form-checkbox>
        </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
    </b-form>
    </b-modal>
  </div>
</v-layout>

</template>

<script>
/* eslint-disable */
import axios from 'axios';
import Alert from './Alert';
import NavBar from './NavBar'

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: "",
        author: "",
        available: "",
      },
      editForm: {
        _id: "",
        title: "",
        author: "",
        available: "",
      },
      message: "",
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
    'navbar': NavBar
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
      .then((res) => {
        this.books = res.data.books;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    editBook(book) {
      this.editForm = book;
    },
    updateBook(payload, bookID) {
    const path = `http://localhost:5000/books/${bookID}`;
    axios.put(path, payload)
      .then(() => {
        this.getBooks();
        this.message = 'Book updated!';
        this.showMessage = true;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.getBooks();
      });
    },
    removeBook(bookID) {
    const path = `http://localhost:5000/books/${bookID}`;
    axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook(book) {
      this.removeBook(book._id);
    },

    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      this.initForm();
      this.getBooks(); // why?
    },

    initForm() {
      this.addBookForm.title = "";
      this.addBookForm.author = "";
      this.addBookForm.available = [];
      this.editForm._id = "";
      this.editForm.title = "";
      this.editForm.author = "";
      this.editForm.available = [];
    },

    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let available = false;
      if (this.addBookForm.available[0]) available = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        available, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      let available = false;
      if (this.editForm.available[0]) available = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        available,
      };
      this.updateBook(payload, this.editForm._id);
    },

    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getBooks();
  },
};
</script>

<style>
#books form label{
  color:black;
}
</style>