
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import Vuetify from 'vuetify'
import './plugins/vuetify'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import colors from 'vuetify/es5/util/colors'

import App from './App';
import router from './router';

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(Vuetify, {
  theme: {
    primary: colors.grey.darken2,
    secondary: colors.grey.darken3,
    backcolor: colors.grey.darken4,
    accent: colors.shades.black,
    error: colors.red.accent3
  }

})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
