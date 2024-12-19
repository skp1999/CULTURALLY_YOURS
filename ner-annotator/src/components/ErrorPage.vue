<template>
    <div class="error-page">
      <h1>Error 404</h1>
      <p>Sorry, the page you are looking for does not exist.</p>
      <q-btn
      @click="handleRestart()"
        >Restart</q-btn>
    </div>
  </template>
  
  <script>
  export default {
    name: "ErrorPage",
    methods:{
    handleRestart(){
        window.location.reload();
    },
    }
  };
  </script>
  
  <style scoped>
  .error-page {
    text-align: center;
    margin-top: 100px;
  }
  </style>
  