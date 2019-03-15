import Vue from 'vue';
import Router from 'vue-router';
import Login from '@/components/Login'
import Register from '@/components/Register'
import Dashboard from '@/components/Dashboard'
import Books from '@/components/Books';
import Profile from '../components/Profile';
import Searchfield from "../components/Searchfield";

Vue.use(Router);

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
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

export default router;