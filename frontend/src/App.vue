<template>
  <div id="app">
    <DataStream />
  </div>
</template>

<script>
import DataStream from "./components/DataStream.vue";

export default {
  name: "App",
  components: {
    DataStream
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
