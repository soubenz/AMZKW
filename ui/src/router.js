import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import store from './store';

Vue.use(Router)

let router = new Router({
  routes: [{
      path: '/',
      // name: '',
      redirect: 'app'
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import( /* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('./views/Signup.vue')

    },
    {
      path: '/signin',
      name: 'signin',
      component: () => import('./views/Signin.vue')

    },
    {
      path: '/app',
      name: 'app',
      component: () => import('./views/App.vue'),
      meta: {
        auth: true
      }

    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.meta.auth && !store.state.currentUser) {
    next({
      path: '/signin'
    })
  } else {
    next()
  }

})


export default router