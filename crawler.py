# Web Crawler pour Apprentissage Autonome
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited = set()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def crawl(self, search_term):
        try:
            search_url = f"https://fr.wikipedia.org/w/api.php?action=query&titles={{search_term}}&format=json&prop=extracts"
            response = requests.get(search_url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                pages = data.get('query', {}).get('pages', {})
                
                for page_id, page_data in pages.items():
                    extract = page_data.get('extract', '')
                    if extract:
                        return extract[:500]
            
            return f"Information sur {{search_term}} non disponible"
            
        except Exception as e:
            return f"Erreur lors du crawling: {{str(e)}}"

    def is_valid_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
