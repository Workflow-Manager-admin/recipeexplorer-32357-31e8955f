<template>
  <teleport to="body">
    <div class="overlay" @click.self="$emit('close')">
      <div class="modal">
        <button class="close-btn" :style="accentBtn" @click="$emit('close')">✕</button>
        <div v-if="recipe" class="modal-content">
          <div class="modal-header">
            <h2>{{ recipe.title }}</h2>
            <div class="recipe-tags">
              <span v-for="tag in recipe.tags || []" :key="tag" class="tag">{{ tag }}</span>
            </div>
          </div>
          <img v-if="recipe.image" :src="recipe.image" alt="recipe-cover" class="detail-img" />
          <div class="meta">
            <span class="label">Author:</span>
            <span>{{ recipe.author || "Unknown" }}</span>
          </div>
          <div class="meta" v-if="recipe.ingredients">
            <span class="label">Ingredients:</span>
            <ul>
              <li v-for="ing in recipe.ingredients" :key="ing">{{ ing }}</li>
            </ul>
          </div>
          <div class="meta" v-if="recipe.instructions">
            <span class="label">Instructions:</span>
            <ol>
              <li v-for="step in recipe.instructions" :key="step">{{ step }}</li>
            </ol>
          </div>
        </div>
      </div>
    </div>
  </teleport>
</template>
<script setup lang="ts">
import { defineProps } from "vue";
const props = defineProps({ recipe: Object });
const accentBtn = "background:#E91E63;color:#fff;";
</script>
<style scoped>
.overlay {
  position: fixed; top:0; left:0; width: 100vw; height:100vh;
  background: rgba(0,0,0,0.14); z-index:50;
  display: flex; justify-content:center; align-items:center;
}
.modal {
  background: #fff;
  border-radius: 10px;
  max-width: 430px; padding: 2.1rem 1.2rem 1.25rem 1.2rem;
  box-shadow: 0 5px 32px 2px #E91E6337, 0 0px 2.5px #0001;
  min-width: 300px;
  position: relative;
}
.close-btn {
  position: absolute; right: 1.3rem; top: 1.07rem;
  border: none; border-radius: 6px; font-size:1.13rem;
  padding: 0.1rem 0.5rem; cursor: pointer; font-weight: 700;
}
.modal-content { margin-top:0.3rem; }
.modal-header { display: flex; flex-direction: column; align-items: flex-start; }
h2 { font-weight: bold; margin-bottom: 0.37rem; }
.recipe-tags { margin-bottom: 0.6rem; }
.tag {
  background: #E91E63;
  color: #fff;
  border-radius: 3.5px;
  font-size: 0.9rem;
  padding: 0.14rem 0.48rem;
  margin-right:0.23rem;
}
.detail-img {
  width: 100%; border-radius: 7px; object-fit: cover; margin: 0.5rem 0 1.3rem 0;
}
.meta { margin-bottom: 1.05rem; }
.label { font-weight: 500; margin-right: 0.6rem; color:#4CAF50;}
ul,ol { padding-left: 1.3rem; margin: 0.21rem 0 0.4rem 0; }
@media (max-width:600px){
  .modal { max-width:99vw; min-width:0; padding:1.1rem 0.3rem;}
}
</style>
