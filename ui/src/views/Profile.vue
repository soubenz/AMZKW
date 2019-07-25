<template>
  <section class="section">
    <div class="container has-background-grey-light">
      <h1>Keyword Generator</h1>
      <div>
        <template v-if="!isLoading">
          <b-field>
            <b-input placeholder="Seed Keyword" size="is-large" expanded></b-input>
            <b-button type="is-primary" @click="isLoading = !isLoading" size="is-large">Start</b-button>
            <b-button type="is-primary" @click="getID" size="is-large">test</b-button>
            <b-button type="is-primary" @click="getKeywords" size="is-large">keywords</b-button>
          </b-field>
        </template>
        <template v-else>
          <b-field>
            <b-input placeholder="Generating keywords ..." size="is-large" loading expanded></b-input>
            <b-button type="is-danger" @click="isLoading = !isLoading" size="is-large">Stop</b-button>
          </b-field>
        </template>
        <template v-if="isLoading"></template>
      </div>
      <div class="columns has-margin-top-10">
        <b-field
          class="column is-one-quarter"
          label="Keywords Number"
          horizontal
          grouped
          custom-class="is-medium"
        >
          <b-select placeholder="Select a limit" size="is-medium" required>
            <option value="20">20</option>
            <option value="50">50</option>
            <option value="100">100</option>
          </b-select>
        </b-field>
        <b-checkbox
          size="is-medium"
          custom-class="is-large"
          type="is-info"
          class="title column is-one-quarter"
        >Only longtails</b-checkbox>
      </div>
      <div>
        <b-notification
          :closable="false"
          position="is-bottom-left"
          :active.sync="isLoading"
        >Please wait while the tool is generating keywords</b-notification>
      </div>
    </div>
    <!-- <template v-else>
    </template>-->
  </section>
</template>


<script>
import database from "@/services/database";
import api from "@/services/api";
// import APIService from "@/services/api";
import axios from "axios";

export default {
  name: "profile",
  computed: {
    currentUser() {
      return this.$store.state.currentUser;
    }
  },
  methods: {
    setIsLoading(state) {
      this.isLoading = state;
      console.log(this.isLoading);
    },
    async getID() {
      let result = await database.getID();
      console.log(result);
    },

    async getKeywords(keywords, limit) {
      api
        .get("/run")
        // const API_URL = "http://localhost:3000";
        // const url = API_URL + "/run";
        // let token = await database.getID();
        // console.log(token);

        // axios
        //   .get(url, {
        //     headers: { Authorization: "bearer " + token },
        //     params: {
        //       keyword: "milk",
        //       limit: 10
        //     }
        //   })
        // .then(response => response.data)
        .then(data => {
          console.log(data);
        });
    }
  },
  data() {
    return {
      isLoading: false
    };
  }
};
</script>
<style>
body * {
  color: hsla(210, 100%, 100%, 0.88) !important;
  background: hsla(210, 100%, 50%, 0.33) !important;
  outline: 0.25rem solid hsla(210, 100%, 100%, 0.5) !important;
}
</style>;
