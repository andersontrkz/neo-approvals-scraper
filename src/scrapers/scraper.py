from parsel import Selector
import requests


class Scraper:
    base_url = ''

    def fetch_url(self, url_path):
        response = ""
        fetch_to_url = self.base_url + url_path
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

    def scrape_get(self, html_content, selector_tag):
        selector = Selector(html_content)
        element = selector.css(selector_tag).get()
        return element

    def scrape_getall(self, html_content, selector_tag):
        selector = Selector(html_content)
        elements = selector.css(selector_tag).getall()
        return elements
