<template>
  <GeneratePDF> </GeneratePDF>
</template>

<script>
import GeneratePDF from "@/components/GeneratePDF";

export default {
  name: 'App',
  components: {
    GeneratePDF
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
