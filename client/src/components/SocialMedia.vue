<template>
  <v-layout>
    <v-flex>
      <v-btn fab dark small color="grey">
        <facebook url="https://www.facebook.com/"></facebook>
      </v-btn>
      <v-btn fab dark small color="grey">
        <twitter url="https://twitter.com/"></twitter>
      </v-btn>
      <v-btn fab dark small color="grey">
        <linkedin url="https://www.linkedin.com"></linkedin>
      </v-btn>
      <v-btn fab dark small color="grey">
        <telegram url="https://www.telegram.com/"></telegram>
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import { Facebook } from 'vue-socialmedia-share';
import { Twitter } from 'vue-socialmedia-share';
import { Linkedin } from 'vue-socialmedia-share';
import { Reddit } from 'vue-socialmedia-share';
import { Telegram } from 'vue-socialmedia-share';
import { WhatsApp } from 'vue-socialmedia-share';
import { Pinterest } from 'vue-socialmedia-share';
import { Google } from 'vue-socialmedia-share';
import { Email } from 'vue-socialmedia-share';

// usage in local component

export default {
  components: {
    Facebook,Twitter,Linkedin,Reddit,Telegram,WhatsApp,Pinterest,Google,Email
  }
};
</script>