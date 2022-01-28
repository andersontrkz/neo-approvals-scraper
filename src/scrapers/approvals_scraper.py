import timeit
from time import sleep

from scrapers.scraper import Scraper
from cleaners.cleaner import Cleaner
from validators.cpf_validator import CpfValidator
from database.models.approvals_model import ApprovalsModel
from threads.multithread import Multithread


class ApprovalsScraper(Scraper):
    approvals_list = []
    initial_page = 1
    last_page = 4672
    base_url = 'https://sample-university-site.herokuapp.com'
    selectors = {
      'cpf_list': 'body > li > a ::text',
      'cpf_paths': 'body > li > a ::attr(href)',
      'next_page_path': 'body > div > a ::attr(href)',
      'approval_data': 'body > div ::text',
    }

    @classmethod
    def scrape_approval_by_cpf(cls, cpf):
        if (CpfValidator.validate(cpf)):
            approval_html = cls.fetch_url(f'/candidate/{cpf}')
            if (approval_html):
                approval_data = cls.scrape_getall(approval_html, cls.selectors['approval_data'])

                name = Cleaner.name_cleaning(approval_data[1])
                score = Cleaner.score_cleaning(approval_data[3])
                cpf = Cleaner.cpf_cleaning(cpf)

                cls.approvals_list.append([cpf, name, score])
                print(f'Add... {cpf} | Total: {len(cls.approvals_list)}')

            else:
                cls.scrape_approval_by_cpf(cpf)

    @classmethod
    def scrape_approvals_on_html(cls, approvals_html):
        cpf_list = cls.scrape_getall(approvals_html, cls.selectors['cpf_list'])
        for cpf in cpf_list:
            Multithread.initialize(cls.scrape_approval_by_cpf, cpf)

    @classmethod
    def scrape_get_html_content(cls, path):
        html_content = cls.fetch_url(path)
        if (html_content):
            cls.scrape_approvals_on_html(html_content)
        else:
            cls.scrape_get_html_content(path)

    @classmethod
    def initialize_runtime(cls):
        setup_import = ("from scrapers.approvals_scraper import ApprovalsScraper")
        time = timeit.timeit('ApprovalsScraper().initialize()', setup=f'{setup_import}', number=1)
        print(f'Runtime: {time}s')

    @classmethod
    def initialize(cls):
        for index in range(cls.initial_page, cls.last_page):
            print(f'Scraping...: Page {index}')
            Multithread.initialize(cls.scrape_get_html_content, f'/approvals/{index}')

            print(f'Page {index} collected data successfully')
            sleep(0.25)

        while Multithread().active_threads() > 0:
            if Multithread().active_threads() < 2:
                print('Saving approvals...')
                ApprovalsModel.insert_approvals(cls.approvals_list)
                break
