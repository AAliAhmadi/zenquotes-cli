import os
import requests
from dotenv import load_dotenv

load_dotenv()

class QuoteFetcher:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("ZENQUOTES_API_KEY")
        self.base_url = "https://zenquotes.io/api"
        self._quote = ""
        self._author = ""

    def _fetch(self, url):
        try:
            if self.api_key:
                url += f"?apikey={self.api_key}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching quote: {e}")
        return None

    def get_random(self):
        data = self._fetch(f"{self.base_url}/random")
        if data:
            self._quote = data[0]['q']
            self._author = data[0]['a']

    def get_today(self):
        data = self._fetch(f"{self.base_url}/today")
        if data:
            self._quote = data[0]['q']
            self._author = data[0]['a']

    def get_by_author(self, author):
        url = f"{self.base_url}/quotes/author/{author.replace(' ', '%20')}"
        data = self._fetch(url)
        if data and isinstance(data, list):
            self._quote = data[0].get('q', 'No quote found.')
            self._author = data[0].get('a', author)
        else:
            print("❌ No quotes found for that author.")

    def display_quote(self):
        if self._quote and self._author:
            print(f'\n -> "{self._quote}"\n— {self._author}')

        else:
            print("⚠️ No quote to display.")

    @staticmethod
    def list_authors():
        print("\n🔍 Popular authors you can try:")
        print(" - Albert Einstein")
        print(" - Mark Twain")
        print(" - Maya Angelou")
        print(" - Confucius")
        print(" - Oscar Wilde")
        print(" - Steve Jobs")
