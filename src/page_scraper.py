```python
import requests
from bs4 import BeautifulSoup, Comment

class PageScraper:
    def __init__(self):
        pass

    def is_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def scrape_page(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        texts = soup.findAll(text=True)
        visible_texts = filter(self.is_visible, texts)

        return " ".join(t.strip() for t in visible_texts)
```