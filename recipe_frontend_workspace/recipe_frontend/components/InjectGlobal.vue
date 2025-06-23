<script setup lang="ts">
import { ref, provide } from "vue";
const user = ref(null);
function setUser(u) { user.value = u; }
function logout() { user.value = null; }
provide("user", user);
provide("setUser", setUser);
provide("logout", logout);
</script>
<template><slot /></template>
