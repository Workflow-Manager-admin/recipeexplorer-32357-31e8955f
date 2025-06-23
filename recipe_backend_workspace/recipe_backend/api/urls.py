from django.urls import path
from .views import (
    health,
    RegisterView,
    LoginView,
    RecipeListCreateView,
    RecipeDetailView,
    SearchRecipeView,
)

urlpatterns = [
    path('health/', health, name='Health'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('recipes/', RecipeListCreateView.as_view(), name='recipes-list-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/search/', SearchRecipeView.as_view(), name='recipes-search'),
]
