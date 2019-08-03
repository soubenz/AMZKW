import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import firebase from 'firebase'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import axios from 'axios'

Vue.config.productionTip = false

Vue.use(Buefy)
let app

const initialize = () => {
  if (!app) {
    new Vue({
      router,
      store,
      render: h => h(App)
    }).$mount('#app')
  }


}


firebase.auth().onAuthStateChanged(user => {
  if (user) {
    store.commit('setCurrentUser', user)
  } else {
    store.commit('setCurrentUser', null)
  }
  initialize()
})



axios.interceptors.request.use(async config => {
  const token = await firebase.auth().currentUser.getIdToken();
  config.headers.Authorization = `Bearer ${token}`
  console.log(config.headers.Authorization)
  return config
}, (error) => {
  return Promise.reject(error)
})