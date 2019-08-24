<template>
  <div id="app">
    <!-- <link rel="stylesheet" href="https://cdn.materialdesignicons.com/2.5.94/css/materialdesignicons.min.css"> -->
    <b-navbar id="nav">
      <template slot="brand">
        <b-navbar-item href="/">
          <img src="@/assets/logo.png" alt="Keyword Stormer" />
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item href="#">
          <strong>About</strong>
        </b-navbar-item>
      </template>

      <template slot="end">
        <b-navbar-item tag="div">
          <div class="buttons">
            <template v-if="!currentUser">
              <b-button type="is-primary">
                <router-link to="/signup" class="link">Sign Up</router-link>
              </b-button>
              <b-button type="is-primary">
                <router-link to="/signin" class="link">Sign In</router-link>
              </b-button>
            </template>
            <template v-else>
              <p class="navbar-item">{{ currentUser.email}}</p>
              <b-button type="is-danger" @click="signOut">Sign out</b-button>
            </template>
            <!-- <strong>Sign up</strong> -->
          </div>
        </b-navbar-item>
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
  padding: 10px;
}
.link {
  color: #ffffff;
}

/* #nav a {
  font-weight: bold;
  color: #e7e9ec;
} */

#nav a.router-link-exact-active {
  color: #ffffff;
}
</style>
