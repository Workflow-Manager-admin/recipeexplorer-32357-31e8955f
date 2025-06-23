<template>
  <div class="login-register-container">
    <div class="card">
      <h2>{{ isRegister ? "Register" : "Login" }}</h2>
      <form @submit.prevent="handleSubmit">
        <input v-model="username" required placeholder="Username" />
        <input v-model="password" type="password" required placeholder="Password" />
        <transition name="fade">
          <input
            v-if="isRegister" v-model="email"
            type="email" required placeholder="Email"
          />
        </transition>
        <button :style="primaryBtn" :disabled="loading">{{ isRegister?"Register":"Login" }}</button>
        <div class="link" @click="toggleMode">
          <span :style="accentColor">
            {{ isRegister ? "Have an account? Login" : "No account? Register" }}
          </span>
        </div>
        <div class="error" v-if="error">{{ error }}</div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, inject } from "vue";
const user = inject("user");
const setUser = inject("setUser");
const isRegister = ref(false);
const username = ref('');
const password = ref('');
const email = ref('');
const error = ref('');
const loading = ref(false);

const primaryBtn = "background:#4CAF50;color:#fff;";
const accentColor = "color:#E91E63;cursor:pointer;text-decoration:underline;";

const API_BASE = import.meta.env.VITE_API_BASE || "https://vscode-internal-947329-qa.qa01.cloud.kavia.ai:3001";

async function handleSubmit() {
  error.value = "";
  loading.value = true;
  try {
    let endpoint = isRegister.value ? "/users/register/" : "/token/";
    let body = isRegister.value
      ? { username: username.value, password: password.value, email: email.value }
      : { username: username.value, password: password.value };
    const res = await fetch(API_BASE + endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    if (!res.ok) {
      let msg = "Unknown error";
      try { msg = (await res.json()).detail || (await res.text()); } catch {}
      throw new Error(msg);
    }
    let data = await res.json();
    if (isRegister.value) {
      // Registration successful, prompt to login
      isRegister.value = false;
      error.value = "Registration successful! Please log in.";
      username.value = ""; password.value = ""; email.value = "";
    } else {
      // Set token/user
      setUser({ username: username.value, token: data.token });
    }
  } catch (e: any) {
    error.value = (e && e.message) || "Error";
  } finally {
    loading.value = false;
  }
}
function toggleMode() {
  isRegister.value = !isRegister.value;
  error.value = "";
}
</script>

<style scoped>
.login-register-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 48vh;
}
.card {
  min-width: 320px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 5px 18px 2px rgba(80,100,120,0.07);
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 370px;
  margin: 1rem;
}
h2 { margin-bottom: 1.2rem; }
form { display: flex; flex-direction: column; width: 100%; }
input {
  margin-bottom: 1rem;
  padding: 0.7rem;
  border: 1px solid #eee;
  border-radius: 5px;
  font-size: 1.07rem;
  transition: border .18s;
}
input:focus { border: 1.5px solid #4CAF50; outline: none;}
button {
  margin-bottom: 0.7rem;
  padding: 0.7rem;
  border: none;
  border-radius: 5px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: opacity 0.18s;
}
button[disabled] { opacity:0.7; }
.link { font-size: 0.97rem; margin-top: 0.5rem; }
.error { color: #E91E63; margin-top: 0.7rem; font-size: 0.98rem;}
.fade-enter-active, .fade-leave-active { transition: opacity .35s;}
.fade-enter-from, .fade-leave-to { opacity: 0;}
@media (max-width: 570px) {
  .card { min-width: 85vw; padding: 0.8rem;}
}
</style>
