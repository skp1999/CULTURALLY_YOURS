<template>
  <div class="loader">
    <div style="display: flex; flex-direction: column; align-items: center; margin: 2%;">
    <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
    <p style="font-size: 1.5rem; text-align: center; color: #555; margin-top: 10px;">
        Please wait while we get your response!
    </p>
    </div>
  </div>
</template>

<script>
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  name: 'Loader',
  components: {
    PulseLoader,
  }

};
</script>

<style scoped>
.loader {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 80vh;
}

.spinner {
  width: 60px;
  height: 60px;
  border: 8px solid transparent;
  border-radius: 50%;
  border-top: 8px solid #3498db;
  border-right: 8px solid rgba(0, 0, 0, 0.1);
  animation: spin 1.2s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
