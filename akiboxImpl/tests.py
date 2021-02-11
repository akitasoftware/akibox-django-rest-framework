# Copyright 2021 Akita Software, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy

from akita_django.test import Client
from django.test import TestCase
from rest_framework import status

from .models import User, File
from .serializers import UserSerializer, FileSerializer


class UserTest(TestCase):
    """Tests for user-related APIs."""

    def setUp(self):
        self.client = Client(har_file_path='akita_trace.user.har')

    def test_user_crud(self):
        kent = {
            "first_name": "Kent",
            "last_name": "Bazemore",
            "email": "kent@warriors.com",
            "phone": "415-111-2233",
        }

        # Create user
        response = self.client.post('/users/', kent, content_type="application/json")
        expected = copy.deepcopy(kent)
        expected["id"] = response.data["id"]

        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get user
        response = self.client.get(f'/users/{expected["id"]}/')
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update user
        expected["phone"] = "415-999-8877"
        response = self.client.put(f'/users/{expected["id"]}/', data=expected, content_type='application/json')
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete user
        response = self.client.delete(f'/users/{expected["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Try to get user, should fail
        response = self.client.get(f'/users/{expected["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        self.client.close()


class FileTest(TestCase):
    """Tests for file-related APIs."""

    def setUp(self):
        self.client = Client(har_file_path='akita_trace.file.har')

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
        response = self.client.post('/files/', chriss, content_type="application/json")
        expected = copy.deepcopy(chriss)
        expected["id"] = response.data["id"]
        expected["created_at"] = response.data["created_at"]

        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get file
        response = self.client.get(f'/files/{expected["id"]}/')
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update file 
        expected["contents"] = "Whoops deleted lol."
        response = self.client.put(f'/files/{expected["id"]}/', data=expected, content_type='application/json')
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete file
        response = self.client.delete(f'/files/{expected["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Try to get file, should fail
        response = self.client.get(f'/files/{expected["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        self.client.close()

