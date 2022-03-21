import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry


class Scraper:
    base_url = ''

    @classmethod
    def fetch_url(cls, url_path):
        fetch_to_url = cls.base_url + url_path
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('https://', adapter)
        response = session.get(fetch_to_url)

        return response.text

    @classmethod
    def scrape_soup(cls, fetch_path):
        html_content = cls.fetch_url(fetch_path)
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

    @classmethod
    def scrape_get(cls, soup_content, soup_tag):
        element = soup_content.find(soup_tag)
        return element

    @classmethod
    def scrape_getall(cls, soup_content, soup_tag):
        elements = soup_content.find_all(soup_tag)
        return elements
