<template>
  <div id="app">
    <!-- <link rel="stylesheet" href="https://cdn.materialdesignicons.com/2.5.94/css/materialdesignicons.min.css"> -->
    <b-navbar>
        <template slot="brand">
            <b-navbar-item href="/">
                <img
                    src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
                    alt="Lightweight UI components for Vue.js based on Bulma"
                >
            </b-navbar-item>
        </template>
        <template slot="start">
            <b-navbar-item href="#">
                About
            </b-navbar-item>
        </template>

        <template slot="end">

            <div class="buttons">
              <template  v-if="!currentUser">
                <b-button type="is-primary">
                  <router-link  class="navbar-item" to="/signup">Sign Up</router-link>
                </b-button>
                <b-button type="is-light">
                  <router-link class="navbar-item"  to="/signin">Sign In</router-link>
                </b-button>
              </template>
              <template v-else>
                <p  class="navbar-item">{{ currentUser.email}}</p>
                <b-button  class="navbar-item" type="is-danger" @click="signOut">Sign out</b-button>
              </template>
              <!-- <strong>Sign up</strong> -->

          </div>
        </template>
    </b-navbar>

    <router-view />
  </div>
</template>



<script>
import database from "@/services/database";
import "bulma-helpers/css/bulma-helpers.css";

export default {
  computed: {
    currentUser() {
      return this.$store.state.currentUser;
    }
  },
  methods: {
    async signOut() {
      await database.signOut();
      this.$router.push("/signin");
    }
  }
};
</script>
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
