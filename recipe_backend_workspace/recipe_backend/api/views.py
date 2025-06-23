from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, generics
from rest_framework.views import APIView
from django.contrib.auth import login
from django.db.models import Q
from .models import Recipe
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    RecipeSerializer,
)


@api_view(['GET'])
def health(request):
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class RegisterView(APIView):
    """User registration endpoint."""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'username': user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PUBLIC_INTERFACE
class LoginView(APIView):
    """User login endpoint."""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({'username': user.username})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PUBLIC_INTERFACE
class RecipeListCreateView(generics.ListCreateAPIView):
    """List all recipes or create a new recipe."""
    queryset = Recipe.objects.all().order_by('-created_at')
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# PUBLIC_INTERFACE
class RecipeDetailView(generics.RetrieveAPIView):
    """Retrieve a specific recipe by ID."""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]


# PUBLIC_INTERFACE
class SearchRecipeView(generics.ListAPIView):
    """Search recipes by title or ingredients."""
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Recipe.objects.all().order_by('-created_at')
        query = self.request.query_params.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(ingredients__icontains=query)
            )
        return queryset
