<template>
  <div class="hello-data">
    <h2>les data</h2>
    <ul>
      <li v-for="dataPoint in basicModel" :key="dataPoint.index">
        {{ dataPoint }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloData",
  data() {
    return {
      basicModel: [], // Array for holding the basicModel data
    };
  },
  created() {
    // This will be called when HelloWorld is loaded
    this.getData(); // Call our getData function below
  },
  methods: {
    getData() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/basic-model/",
      }).then((response) => (this.basicModel = response.data));
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
