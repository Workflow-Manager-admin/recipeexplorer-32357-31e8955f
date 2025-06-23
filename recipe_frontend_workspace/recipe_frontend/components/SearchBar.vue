<template>
  <div class="search-bar">
    <input
      v-model="q"
      placeholder="Search recipes (e.g. pasta, vegan, chicken)..."
      @input="emitSearch"
      :style="searchInput"
    />
    <button :style="searchBtn" @click="emitSearch"><span>🔍</span></button>
  </div>
</template>

<script setup lang="ts">
import { ref, defineEmits } from "vue";
const emit = defineEmits(["search"]);
const q = ref("");
const searchInput = "border:1.4px solid #E91E63;padding:0.4rem 1rem; border-radius: 5px 0 0 5px; font-size: 1.07rem;";
const searchBtn = "background:#4CAF50;color:#fff;border:none;border-radius:0 5px 5px 0;padding:0.4rem 0.9rem;font-size:1.07rem;cursor:pointer;";
function emitSearch() { emit("search", q.value); }
</script>

<style scoped>
.search-bar {
  display: flex; align-items: center; gap: 0;
  margin-bottom: 1.1rem;
}
input { outline: none; }
button:hover { opacity:0.86;}
@media (max-width: 600px) { .search-bar { width: 100%; } }
</style>
