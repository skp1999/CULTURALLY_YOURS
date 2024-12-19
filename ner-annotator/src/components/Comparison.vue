<template>
  <div class="comparison-page">
    <div class="content-wrapper">
      <div class="box">
        <div class="scrollable-content">
          <Text class="heading">Initial Annotations<br/></Text>
          <component
            :is="t.type === 'token' ? 'Token' : 'TokenBlock'"
            v-for="t in this.tokens_initial"
            :id="'t' + t.start"
            :key="t.start"
            :token="t"
            :background-color="t.backgroundColor"
            style="margin-top:5px ;"
            @remove-block="onRemoveBlock"
          />
        </div>
      </div>
      <div class="box">
        <div class="scrollable-content">
          <Text class="heading">Updated Annotations<br/></Text>
          <component
            :is="t.type === 'token' ? 'Token' : 'TokenBlock'"
            v-for="t in this.tokens_final"
            :id="'t' + t.start"
            :key="t.start"
            :token="t"
            :background-color="t.backgroundColor"
            style="margin-top:5px ;"
            @remove-block="onRemoveBlock"
          />
        </div>
      </div>
    </div>
    <q-btn class="restart-button" @click="handleRestart">Restart</q-btn>
  </div>
</template>

<script>
import eventBus from './eventBus';
import Token from "./Token";
import TokenBlock from "./TokenBlock";

export default {
  name: 'ComparisonPage',
  components: {
    Token,
    TokenBlock
  },
  data() {
    return {
      tokens_initial: [],
      tokens_final: [],
    };
  },
  mounted() {

    this.tokens_initial = eventBus.value.tokens_initial || [];
    this.tokens_final = eventBus.value.tokens_final || [];

  },
  methods: {
    handleRestart() {
      this.$emit("restart-btn");
      eventBus.value.config = [];
    },
  }
}
</script>

<style scoped>
.comparison-page {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.content-wrapper {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px; 
}

.box {
  flex: 1;
  margin: 0 10px;
  display: flex;
  flex-direction: column;
}

.scrollable-content {
  flex: 1;
  overflow-y: scroll;
  height: 40vh; 
  padding: 20px; 
  box-sizing: border-box;
  min-height: 400px;
  border-radius: 8px; 
  background-color: #ffffff; 
  border: 1px solid #dcdcdc; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
}

.restart-button {
  width: 120px;
  height: 50px;
  margin-top: 20px;
  align-self: center;
  color: #ffffff; 
  background-color: #3c83d9; 
  border: none; 
  border-radius: 4px; 
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1); 
  font-weight: bold; 
  cursor: pointer; 
  transition: background-color 0.3s, box-shadow 0.3s; 
}

.restart-button:hover {
  background-color: #3167a4; 
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); 
}

.heading {
  font-size: 24px; 
  font-weight: bold; 
  color: #333333; 
  margin-bottom: 16px; 
  padding: 10px 0;
  border-bottom: 2px solid #3c83d9; 
  text-align: center; 
}

</style>
