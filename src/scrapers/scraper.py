from bs4 import BeautifulSoup
import requests


class Scraper:
    base_url = ''

    @classmethod
    def fetch_url(cls, url_path):
        response = ""
        fetch_to_url = cls.base_url + url_path
        try:
            response = requests.get(fetch_to_url, timeout=3)
            response.raise_for_status()

        except requests.HTTPError:
            print(response.status_code)
            return None

        finally:
            if response != "" and response.status_code == 200:
                return response.text
            return None

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
