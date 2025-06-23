---
theme: default
name: "Recipe Explorer"
title: "Recipe Explorer"
info: |
  Modern, light-themed recipe discovery web app.
colorSchema:
  primary: "#4CAF50"
  accent: "#E91E63"
  secondary: "#FF9800"
class: text-center
css: "./theme.css"
---

# Recipe Explorer

A modern place to browse, search, and discover delicious recipes.

---

<!-- Top navigation bar, global login/register state -->
<Navbar />

---

# Login or Register

<LoginRegister />

---

layout: two-cols
---

# Browse Recipes

## <SearchBar />

<RecipeGrid />

---

# Recipe Details

<RecipeDetailModal v-if="showDetail" :recipe="selectedRecipe" @close="showDetail=false" />

---

# Thanks for exploring recipes with us!

<PoweredBySlidev mt-10 />

---
