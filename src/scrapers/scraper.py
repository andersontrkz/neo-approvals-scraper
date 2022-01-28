from parsel import Selector
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
            return response.status_code

        finally:
            if response != "" and response.status_code == 200:
                return response.text
            return None

    @classmethod
    def scrape_get(cls, html_content, selector_tag):
        selector = Selector(html_content)
        element = selector.css(selector_tag).get()
        return element

    @classmethod
    def scrape_getall(cls, html_content, selector_tag):
        selector = Selector(html_content)
        elements = selector.css(selector_tag).getall()
        return elements
