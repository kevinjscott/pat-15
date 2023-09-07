import os
import serpyco
import requests

class SerpApiWrapper:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        self.serpapi = serpyco.SerpApiClient(self.api_key)

    def search(self, query):
        params = {
            "engine": "google",
            "q": query,
            "api_key": self.api_key
        }
        response = requests.get('https://api.serpapi.com/search', params)
        return response.json()

    def find_course_profile(self, golf_club, city, state):
        query = f"{golf_club} {city} {state} site:bluegolf.com"
        results = self.search(query)
        for result in results.get('organic_results', []):
            if 'bluegolf.com' in result['link']:
                return result['link']
        return None

    def find_social_media(self, name, team, term="golf"):
        query = f"{name} {team} {term}"
        results = self.search(query)
        social_links = {}
        for result in results.get('organic_results', []):
            if 'twitter.com' in result['link']:
                social_links['twitter'] = result['link']
            elif 'instagram.com' in result['link']:
                social_links['instagram'] = result['link']
            elif 'linkedin.com' in result['link']:
                social_links['linkedin'] = result['link']
        return social_links