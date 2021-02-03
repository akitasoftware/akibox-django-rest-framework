import copy
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import User, File
from .serializers import UserSerializer, FileSerializer

# Initialize the APIClient app
client = Client()


class UserTest(TestCase):
    """Tests for user-related APIs."""

    def test_user_crud(self):
        kent = {
            "first_name": "Kent",
            "last_name": "Bazemore",
            "email": "kent@warriors.com",
            "phone": "415-111-2233",
        }

        # Create user
        response = client.post('/users/', kent)
        expected = copy.deepcopy(kent)
        expected["id"] = response.data["id"]

        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get user
        response = client.get(f'/users/{expected["id"]}/')
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update user
        expected["phone"] = "415-999-8877"
        response = client.put(f'/users/{expected["id"]}/', data=expected, content_type='application/json')
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete user
        response = client.delete(f'/users/{expected["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Try to get user, should fail
        response = client.get(f'/users/{expected["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class FileTest(TestCase):
    """Tests for file-related APIs."""

    def test_file_crud(self):
        chriss = {
            "contents": """Marquese Chriss
Forward

Height:         6'9
Weight:         240lbs
DOB:            07/02/1997
Prior to NBA:   Washington
Country:        USA
Years Pro:      4""",
        }

        # Create file
        response = client.post('/files/', chriss)
        expected = copy.deepcopy(chriss)
        expected["id"] = response.data["id"]
        expected["created_at"] = response.data["created_at"]

        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get file
        response = client.get(f'/files/{expected["id"]}/')
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update file 
        expected["contents"] = "Whoops deleted lol."
        response = client.put(f'/files/{expected["id"]}/', data=expected, content_type='application/json')
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete file
        response = client.delete(f'/files/{expected["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Try to get file, should fail
        response = client.get(f'/files/{expected["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

