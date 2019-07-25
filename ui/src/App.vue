<template>
  <div id="app">
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="https://bulma.io">
          <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28" />
        </a>

        <a
          role="button"
          class="navbar-burger burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbarBasicExample"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">Home</a>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="!currentUser">
                <b-button type="is-primary">
                  <router-link to="/signup">Sign Up</router-link>
                </b-button>
                <b-button type="is-light">
                  <router-link to="/signin">Sign In</router-link>
                </b-button>
              </template>
              <template v-else>
                <p>{{ currentUser.email}}</p>
                <b-button type="is-danger" @click="signOut">Sign out</b-button>
              </template>
              <!-- <strong>Sign up</strong> -->
            </div>
          </div>
        </div>
      </div>
    </nav>

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
