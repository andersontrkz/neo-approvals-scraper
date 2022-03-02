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

    @classmethod
    def get_approval_information(self, element_tag):
        elements = element_tag.contents
        information = elements[1]
        return information

    @classmethod
    def scrape_approval_data_by_cpf(cls, cpf_element):
        cpf = cpf_element.string

        if (CpfValidator.validate(cpf)):
            cpf_link = cpf_element.get('href')
            soup_content = cls.scrape_soup(cpf_link)

            if (soup_content):
                data_elements = cls.scrape_getall(soup_content, 'div')
                name = cls.get_approval_information(data_elements[0])
                score = cls.get_approval_information(data_elements[1])

                name = Cleaner.name_cleaning(name)
                score = Cleaner.score_cleaning(score)
                cpf = Cleaner.cpf_cleaning(cpf)

                cls.approvals_list.append([cpf, name, score])
                print(f'Add... {cpf} | Total: {len(cls.approvals_list)}')

    @classmethod
    def scrape_approvals_cpf_list(cls, soup_content):
        cpf_elements = cls.scrape_getall(soup_content, 'a')

        for cpf_element in cpf_elements:
            Multithread.initialize(
              cls.scrape_approval_data_by_cpf, cpf_element)

    @classmethod
    def scrape_approvals_on_page(cls, path):
        soup_content = cls.scrape_soup(path)

        if (soup_content):
            cls.scrape_approvals_cpf_list(soup_content)
        else:
            cls.scrape_approvals_on_page(path)

    @classmethod
    def initialize(cls):
        for index in range(cls.initial_page, cls.last_page):
            path = f'/approvals/{index}'
            Multithread.initialize(cls.scrape_approvals_on_page, path)
            print(f'Scraping...: Page {index}')

            print(f'Page {index} collected data successfully')
            sleep(0.25)

        while Multithread().active_threads() > 0:
            if Multithread().active_threads() < 2:
                print('Saving approvals...')
                ApprovalsModel.insert_approvals(cls.approvals_list)
                break
