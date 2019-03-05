import Vue from 'vue';
import Router from 'vue-router';
import Books from '@/components/Books';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
  ],
  mode: 'history',
});
