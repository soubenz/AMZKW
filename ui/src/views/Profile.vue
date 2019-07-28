<template>
  <section class="section">
    <!-- <div class="container has-background-grey-light"> -->
    <div class="container ">
      <h1>Keyword Generator</h1>
      <div>
        <template v-if="!isLoading">
          <b-field>
            <b-input placeholder="Seed Keyword" size="is-large" v-model="seedKeyword" expanded></b-input>
            <b-button type="is-primary" @click="getKeywords(seedKeyword, source, size)" size="is-large" :disabled="!startButton">Start</b-button>
            <!-- <b-button type="is-primary" @click="getID" size="is-large">test</b-button> -->
            <b-button type="is-primary" @click="getMetrics(['milk', 'jaws'])" size="is-large">keywords</b-button>
          </b-field>
        </template>
        <template v-else>
          <b-field>
            <b-input placeholder="Generating keywords ..." size="is-large" loading expanded disabled></b-input>
            <b-button type="is-danger" @click="isLoading = !isLoading" size="is-large">Stop</b-button>
          </b-field>
        </template>
        <template v-if="isLoading"></template>
      </div>
      <div class="columns has-margin-top-10">
        <b-field
          class="column is-one-quarter has-margin-top-10"
          label="Source"
          horizontal
          grouped
          custom-class="is-medium"
        >
          <b-select placeholder="Select a source" v-model="source" size="is-medium" required>
            <option value="amazon">Amazon</option>
            <option value="etsy">Etsy</option>
            <option value="youtube">Youtube</option>
          </b-select>
        </b-field>
        <b-field
          class="column is-one-quarter has-margin-top-10"
          label="Size"
          horizontal
          grouped
          custom-class="is-medium"
        >
          <b-select placeholder="Retreived keywords" v-model="size" size="is-medium" required>
            <option value="20">20</option>
            <option value="50">50</option>
            <option value="100">100</option>
          </b-select>
        </b-field>

      </div>
      <div>
        <b-notification
          :closable="false"
          position="is-bottom-left"
          :active.sync="isLoading"
        >Please wait while the tool is generating keywords</b-notification>
      </div>

    <b-field grouped group-multiline>
            <b-select v-model="perPage" size="is-medium" :disabled="!isPaginated">
                <option value="5">5 per page</option>
                <option value="10">10 per page</option>
                <option value="15">15 per page</option>
                <option value="20">20 per page</option>
            </b-select>
            <div class="control is-flex">
                <b-switch size="is-medium"  class="title" v-model="isPaginated">Longtails Only</b-switch>
            </div>
      </b-field>
 <b-table
          :data="data"
          checked-rows.sync="checkedRows"
          checkable
          :checkbox-position="left"
          paginated
          :current-page.sync="currentPage"
          paginationPosition="top"
          aria-next-label="Next page"
          aria-previous-label="Previous page"
          aria-page-label="Page"
          aria-current-label="Current page"
          >

            <template slot-scope="props">
                <b-table-column field="id" width="60" numeric class="has-text-weight-bold is-size-4">
                    {{ data.indexOf(props.row) + 1 }}
                </b-table-column>

                <b-table-column field="keyword"  class="has-text-weight-bold is-size-4">
                    {{ props.row }}
                </b-table-column>

               
            </template>
           
   </b-table>
   
    </div>
    <!-- <template v-else>
    </template>-->

  </section>
</template>


<script>
import api from "@/services/api";

export default {
  name: "profile",
  computed: {
    currentUser() {
      return this.$store.state.currentUser;
    },
    startButton(){
      if(this.seedKeyword && this.source && this.size ){
      return true}
      else {
        return false
      }
    }
  },

  
  methods: {
    setIsLoading(state) {
      this.isLoading = state;
      console.log(this.isLoading);
    },
   
    initForm() {
      this.seedKeyword = null,
      this.source = null,
      this.size = 20
      // this.data = {}

    },
    async getKeywords(keyword, type, limit) {
      this.isLoading = true
      let params = {
        keyword: keyword,
        type: type,
        limit: limit
      }
      api
        .get("/run", {params: params})
        .then(data => {
          this.data = data.data.items
          console.log(data);
          this.isLoading = false
          this.initForm()
        });
    },
    async getMetrics(keywords) {
      let params = {
        keywords: keywords,
      }
      api
        .get("/metrics", {params: params})
        .then(data => {
          // this.data = data.data.items
          console.log(data);
          // this.isLoading = false
          // this.initForm()
        });
    }
  },
  data() {
    return {
      isLoading: false,
      seedKeyword: null,
      source: null,
      size: 20,
      items: null, 
      data: [],
      perPage: 20,
      currentPage: 1,
      checkedRows: []
    };
  }
};
</script>
<style>
/* body * {
  color: hsla(210, 100%, 100%, 0.88) !important;
  background: hsla(210, 100%, 50%, 0.33) !important;
  outline: 0.25rem solid hsla(210, 100%, 100%, 0.5) !important;
} */
</style>;
