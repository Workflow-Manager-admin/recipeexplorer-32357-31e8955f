<template>
  <nav class="navbar">
    <div class="nav-left">
      <span class="logo" :style="primaryColor">🥗</span>
      <span class="title">Recipe Explorer</span>
    </div>
    <div class="nav-center">
      <slot name="center"></slot>
    </div>
    <div class="nav-right">
      <template v-if="user">
        <span>👤 {{ user.username }}</span>
        <button class="nav-btn" :style="accentColor" @click="logout">Logout</button>
      </template>
      <template v-else>
        <span>Welcome!</span>
      </template>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { inject } from "vue";
const user = inject("user");
const logout = inject("logout");

const primaryColor = "color: #4CAF50;";
const accentColor = "background: #E91E63; color: #fff;";
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fff;
  border-bottom: 2px solid #f0f0f0;
  padding: 0.7rem 2rem;
  height: 60px;
  font-family: 'Inter', Arial, sans-serif;
  position: sticky; top: 0; z-index: 20;
}
.nav-left, .nav-center, .nav-right {
  display: flex; align-items: center;
}
.logo {
  font-size: 1.8rem; margin-right: 0.6rem;
}
.title {
  font-weight: bold;
  font-size: 1.2rem;
  letter-spacing: 1px;
}
.nav-btn {
  border: none;
  border-radius: 5px;
  padding: 0.35rem 1rem;
  margin-left: 1rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: opacity 0.2s;
}
.nav-btn:hover { opacity: 0.82; }
@media (max-width: 600px) {
  .navbar { flex-direction: column; padding: 0.5rem 1rem; gap: 5px; height: auto;}
  .title { font-size: 1.05rem;}
}
</style>
