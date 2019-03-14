
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App';
import router from './router';

import AuthPlugin from "./plugins/auth";

Vue.config.productionTip = false;
Vue.use(AuthPlugin);
Vue.use(BootstrapVue);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
