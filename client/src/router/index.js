import Vue from 'vue';
import Router from 'vue-router';
import Login from '@/components/Login'
import Register from '@/components/Register'
import Dashboard from '@/components/Dashboard'
import Books from '@/components/Books';
import Profile from '../components/Profile';
import SearchResults from "../components/SearchResults";
import AboutBook from "../components/AboutBook";

Vue.use(Router);

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { 
      guest: true
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: { 
      guest: true
    }
  },
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/aboutbook',
    name: 'AboutBook',
    component: AboutBook,
    meta: { 
      requiresAuth: true
    }
  },
  {
    path: '/books',
    name: 'Books',
    component: Books,
    meta: { 
      requiresAuth: true
    }
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile,
    meta: { 
      requiresAuth: true
    }
  },
  {
    path: "/search",
    name: "search",
    component: SearchResults
  }
];

const router = new Router({
  mode: 'history',
  routes
});

// router.beforeEach((to, from, next) => {
//   if(to.matched.some(record => record.meta.requiresAuth)) {
//       if (localStorage.getItem('usertoken') == null) {
//         next({
//             path: '/login',
//             params: { nextUrl: to.fullPath }
//         })
//       }
//       else{
//         next()
//       }
//   } else if(to.matched.some(record => record.meta.guest)) {
//       if(localStorage.getItem('usertoken') == null){
//           next()
//       }
//       else{
//           next()
//       }
//   }else {
//       next() 
//   }
//})

export default router;