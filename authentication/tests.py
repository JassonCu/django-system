from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your tests here.

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_register_view(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_view(self):
        # Registra un usuario para realizar la prueba de inicio de sesión
        User.objects.create_user(username='testuser', password='testpassword')

        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_view_authenticated(self):
        # Registra un usuario y obtiene un token para realizar la prueba de perfil autenticado
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        token = Token.objects.create(user=user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        # Asegúrate de tener el nombre correcto de la URL
        response = self.client.post(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
