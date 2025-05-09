#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up ZenQuotes API key
API_KEY = os.getenv("ZENQUOTES_API_KEY")
BASE_URL = "https://zenquotes.io/api"

class QuoteFetcher:
    def __init__(self):
        self._quote = None
        self._author = None

    def fetch(self, endpoint, params=None):
        try:
            headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}
            response = requests.get(f"{BASE_URL}/{endpoint}", params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def get_random(self):
        data = self.fetch("random")
        if data:
            self._quote = data[0]['q']
            self._author = data[0]['a']

    def get_today(self):
        data = self.fetch("today")
        if data:
            self._quote = data['q']
            self._author = data['a']

    def search_author(self, name):
        data = self.fetch(f"quotes/author/{name}")
        if data and isinstance(data, list):
            self._quote = data[0]['q']
            self._author = data[0]['a']
        else:
            print("No quotes found for that author.")

    @property
    def quote(self):
        if self._quote:
            return f"\"{self._quote}\""
        else:
            return "No quote available."

    @property
    def author(self):
        if self._author:
            return f"- {self._author}"
        else:
            return "No author found."

