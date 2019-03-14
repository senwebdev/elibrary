import Vue from 'vue';
import Router from 'vue-router';
import Dashboard from '@/components/Dashboard'
import Books from '@/components/Books';
import Callback from '../components/Callback';
import Profile from '../components/Profile';
import auth from "../auth/authService";
import Searchfield from "../components/Searchfield";

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/books',
    name: 'Books',
    component: Books,
  },
  {
    path: '/callback',
    name: 'callback',
    component: Callback
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile
  },
  {
    path: "/search",
    name: "search",
    component: Searchfield
  }
];

const router = new Router({
  mode: 'history',
  routes
});

router.beforeEach((to, from, next) => {
  if (to.path === "/" || to.path === "/callback" || auth.isAuthenticated()) {
    return next();
  }

  // Specify the current path as the customState parameter, meaning it
  // will be returned to the application after auth
  auth.login({ target: to.path });
});

export default router;