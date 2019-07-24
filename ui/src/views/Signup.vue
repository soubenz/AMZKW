<template>
  <div class="columns">
    <div class="column is-4 is-offset-4">
      <h1>Sign up></h1>

      <form @submit.prevent="signUp">
        <div class="field">
          <input type="email" v-model="email" placeholder="Email" class="input" />
        </div>
        <div class="field">
          <input type="password" v-model="password" placeholder="Password" class="input" />
        </div>
        <button class="button is-primary">Sign up</button>
      </form>
      <div class="message is-danger" v-if="error">
        <div class="message-body">{{ error }}</div>
      </div>
    </div>
  </div>
</template>



<script>
import database from "@/services/database";

export default {
  name: "signup",
  data() {
    return {
      email: "",
      password: "",
      error: ""
    };
  },
  methods: {
    async signUp() {
      let result = await database.signUp(this.email, this.password);
      if (result.message) {
        this.error = result.message;
      } else {
        console.log("User is created");
      }
    }
  }
};
</script>


<style>
@import "~bulma/css/bulma.css";
</style>