import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    currentUser: null,
    test: null
  },
  mutations: {
    setCurrentUser(state, payload) {
      state.currentUser = payload
    },
    setTest(state, payload) {
      state.test = payload
    }
  },


  actions: {

  }
})