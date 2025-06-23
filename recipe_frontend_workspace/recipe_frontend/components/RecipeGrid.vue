<template>
  <div>
    <SearchBar @search="onSearch" />
    <div v-if="loading" class="loading">Loading recipes...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="grid">
      <div
        v-for="recipe in recipes"
        :key="recipe.id"
        class="recipe-card"
        @click="showDetail(recipe)"
        :style="cardStyle"
      >
        <img v-if="recipe.image" :src="recipe.image" alt="image" class="recipe-img" />
        <div class="card-content">
          <div class="recipe-title">{{ recipe.title }}</div>
          <div class="recipe-tags">
            <span v-for="tag in recipe.tags || []" :key="tag" class="tag">{{ tag }}</span>
          </div>
        </div>
      </div>
    </div>
    <RecipeDetailModal v-if="detail" :recipe="detail" @close="detail=null" />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, inject } from "vue";
import SearchBar from "./SearchBar.vue";
import RecipeDetailModal from "./RecipeDetailModal.vue";
const API_BASE = import.meta.env.VITE_API_BASE || "https://vscode-internal-947329-qa.qa01.cloud.kavia.ai:3001";

const recipes = ref([]);
const loading = ref(false);
const error = ref("");
const q = ref("");
const detail = ref(null);

function onSearch(newQ:string) {
  q.value = newQ;
  fetchRecipes();
}

function showDetail(recipe) { detail.value = recipe; }

async function fetchRecipes() {
  loading.value = true; error.value = "";
  try {
    let url = API_BASE + "/recipes/";
    if (q.value) { url += "?search=" + encodeURIComponent(q.value); }
    const res = await fetch(url, { headers: { "Accept":"application/json"}});
    if (!res.ok) throw new Error("Failed to fetch recipes.");
    recipes.value = await res.json();
  } catch (e:any) {
    error.value = (e && e.message) || "Error";
  } finally {
    loading.value = false;
  }
}
fetchRecipes();

const cardStyle =
  "border:1.5px solid #eee;border-radius:12px;box-shadow:0 2.5px 12px 0 rgba(76,175,80,0.07);padding:1.2rem;background:#fff;cursor:pointer;transition:box-shadow .22s;";

</script>

<style scoped>
.grid {
  display: grid;
  gap: 1.4rem;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  margin: 0 auto;
}
.recipe-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  min-height:180px;
  max-width: 340px;
  margin: auto;
  transition: box-shadow 0.18s;
}
.recipe-card:hover { box-shadow: 0 4px 30px #4CAF5050; }
.recipe-img { width: 100%; aspect-ratio: 5/3; object-fit: cover; border-radius:8px; margin-bottom:0.6rem;}
.card-content { width: 100%;}
.recipe-title {
  font-size: 1.15rem; font-weight: 600; margin-bottom: 0.2rem;
}
.recipe-tags {
  margin-top: 0.4rem; display: flex; flex-wrap: wrap; gap: 0.35rem;
}
.tag {
  background: #E91E63;
  color: #fff;
  border-radius: 3.5px;
  font-size: 0.9rem;
  padding: 0.14rem 0.48rem;
}
.loading { font-size: 1.2rem; margin: 2rem auto;}
.error { color: #E91E63; margin: 1.5rem auto; }
@media (max-width:600px) { .grid { gap:0.7rem;}}
</style>
