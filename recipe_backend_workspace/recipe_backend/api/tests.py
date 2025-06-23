from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class HealthTests(APITestCase):
    def test_health(self):
        url = reverse('Health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Server is up!"})


class RegistrationAndRecipeTests(APITestCase):

    def test_user_registration_and_login(self):
        # Registration
        response = self.client.post(reverse('register'), {
            "username": "testuser",
            "password": "securepass"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["username"], "testuser")

        # Login
        response = self.client.post(reverse('login'), {
            "username": "testuser",
            "password": "securepass"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "testuser")

    def test_recipe_creation(self):
        User.objects.create_user(username='user2', password='pw12345')
        self.client.login(username='user2', password='pw12345')
        response = self.client.post(reverse('recipes-list-create'), {
            "title": "Apple Pie",
            "description": "Classic dessert.",
            "ingredients": "apples\nsugar\npie crust",
            "instructions": "Peel apples.\nMake crust.\nBake."
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Apple Pie")
        self.assertEqual(response.data["created_by"], "user2")
