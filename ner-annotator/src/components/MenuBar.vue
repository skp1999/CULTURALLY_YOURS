<template>
    <div>
      <nav class="navbar">
        <div class="navbar-title" style="cursor: pointer;"
        @click="handleRestart()">
        CULTURALLY YOURS
        </div>
      </nav>
    </div>
  </template>
  
  <script>
import eventBus from './eventBus';


export default {
    name: 'NavBar',
    data() {
        return {
            config: [],
        };
    },

    emits: ["main-page"],
    mounted(){
        this.config = eventBus.value.config || [];
    },
    
    methods: {
        handleRestart(){
          this.$emit('main-page');
          window.location.reload();
          eventBus.value.config = [];
        }

        
    },
  };
  </script>
  
  <style scoped>
.navbar {
  display: flex;
  justify-content: center;  
  align-items: center;      
  padding: 1rem;
  background-color: #f7f7f7;  
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  
  border-bottom: 1px solid #ddd; 
  height: 70px; 
}

.navbar-title {
  color: #4a4a4a;  
  
  font-size: 2rem;  
  font-weight: 600; 
  font-family: 'Roboto', sans-serif; 
  letter-spacing: 1px;
  text-transform: uppercase; 
}

.navbar-title:hover {
  color: #333; 
  transition: color 0.3s ease;  
}
  </style>
  