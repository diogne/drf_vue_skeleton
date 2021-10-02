<template>
  <div class="hello-form">
    <h2>formulaire de base pour ajouter un mot dans le basic model.</h2>

    <form action="">
      <input v-model="newBasicData.word" placeholder="tapez un mot" />
      <p>Le mot est : {{ newBasicData.word }}</p>
      <p>the newBasicData is : {{ newBasicData }}</p>

      <button @click="saveData">validate</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { CSRF_TOKEN } from "../common/csrf_token.js";

export default {
  name: "HelloForm",
  data() {
    return {
      newBasicData: {
        word: "test",
      },
    };
  },
  methods: {
    saveData() {
      console.log("let's go");
      axios({
        method: "POST",
        url: "http://127.0.0.1:8000/api/basic-model/",
        headers: {
          "X-CSRFTOKEN": CSRF_TOKEN,
        },
        data: this.newBasicData,
      })
        .then(function (response) {
          console.log(response.json());
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
