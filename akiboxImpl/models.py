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

import uuid
from django.db import models


class User(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid1(), primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=128)

    class Meta:
        ordering = ['last_name']


class File(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid1(), primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()

    class Meta:
        ordering = ['created_at']

