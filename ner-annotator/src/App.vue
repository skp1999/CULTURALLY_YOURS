<template>
  <div
  class="fullscreen"
  style="overflow-y:scroll;"
  >
  <NavBar
  @main-page="switchToPage('start')"
  />
    <div :style="{'pointer-events': overlayActive ? 'none' : 'auto'}">
      <q-layout view="hHh lpR fFf">

        <q-page-container>
          <start-page
            v-if="currentPage === 'start'"
            @file-loaded="switchToPage('annotate')"
            @error-page="switchToPage('error')"
          />
          
        <annotation-page
            v-if="currentPage === 'annotate'" 
            @review-spans="switchToPage('start')"
          />

          <error-page
            v-if="currentPage === 'error'"
          />

        
      </q-page-container>
      </q-layout>
      <drag-n-drop-overlay :style="{'visibility': overlayActive && pendingFileDrop == null ? 'visible' : 'hidden'}" />
      <exit-dialog
        :show="pendingFileDrop != null && currentPage != 'start'"
        @hide="pendingFileDrop = null"
        @confirm="processFileDrop()"
      />
    </div>
  </div>
</template>

<script>
import StartPage from "./components/StartPage.vue";
import AnnotationPage from "./components/AnnotationPage.vue";
import NavBar from "./components/MenuBar.vue";
import ErrorPage from "./components/ErrorPage.vue";

import { mapState, mapMutations } from "vuex";

export default {
  name: "LayoutDefault",
  _components: {
    StartPage,
    AnnotationPage,
    NavBar,
    ErrorPage
  },
  get components() {
    return this._components;
  },
  set components(value) {
    this._components = value;
  },
  setup() {
  },
  data() {
    return {
      currentPage: "start",
      overlayActive: false,
      pendingFileDrop: null,
    };
  },
  computed: {
    ...mapState(["annotations", "classes"]),
  },

  methods: {
    ...mapMutations(["loadClasses", "loadAnnotations", "setInputSentences", "clearAllAnnotations", "resetIndex"]),
    switchToPage(page) {      
      this.currentPage = page;
    },
  },
};
</script>
