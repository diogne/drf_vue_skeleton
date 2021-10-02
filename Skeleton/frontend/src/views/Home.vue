<template>
  <div class="home">
    <HelloData />
    <HelloForm />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloData from "@/components/HelloData.vue";
import HelloForm from "@/components/HelloForm.vue";

export default {
  name: "Home",
  components: {
    HelloData,
    HelloForm,
  },
};
</script>
