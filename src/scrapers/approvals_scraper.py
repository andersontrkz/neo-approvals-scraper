from validators.cpf_validator import CpfValidator
from scrapers.scraper import Scraper
from cleaners.cleaner import Cleaner


class ApprovalsScraper(Scraper):
    approvals_data = []
    page_path = '/approvals/1'
    base_url = 'https://sample-university-site.herokuapp.com'
    selectors = {
      'cpf_list': 'body > li > a ::text',
      'cpf_paths': 'body > li > a ::attr(href)',
      'next_page_path': 'body > div > a ::attr(href)',
      'approval_data': 'body > div ::text',
    }

    def scrape_approvals_on_html(self, approvals_html):
        cpf_list = self.scrape_getall(approvals_html, self.selectors['cpf_list'])

        for cpf in cpf_list:
            if (CpfValidator.validate(cpf)):
                approval_html = self.fetch_url(f'/candidate/{cpf}')
                approval_data = self.scrape_getall(approval_html, self.selectors['approval_data'])

                name = Cleaner.name_cleaning(approval_data[1])
                score = Cleaner.score_cleaning(approval_data[3])
                cpf = Cleaner.cpf_cleaning(cpf)

                self.approvals_data.append({'cpf': cpf, 'name': name, 'score': score})

    def scrape_approvals_all_pages(self):
        while True:
            approvals_html = self.fetch_url(self.page_path)
            self.scrape_approvals_on_html(approvals_html)
            next_page_path = self.scrape_get(approvals_html, self.selectors['next_page_path'])

            if not next_page_path:
                break

            self.page_path = next_page_path
            print(f'Running: {len(self.approvals_data)} `valid` CPFs successfully collected')
