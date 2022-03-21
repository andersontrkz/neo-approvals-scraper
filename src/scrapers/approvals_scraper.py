from scrapers.scraper import Scraper
from cleaners.cleaner import Cleaner
from validators.cpf_validator import CpfValidator
from threads.multithread import Multithread


class ApprovalsScraper(Scraper):
    approvals_list = []
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

                length = len(cls.approvals_list)
                print(f'Add... {cpf} | Total: {length}')

    @classmethod
    def scrape_approvals_cpf_list(cls, soup_content):
        cpf_elements = cls.scrape_getall(soup_content, 'a')
        for cpf in cpf_elements:
            Multithread.initialize(cls.scrape_approval_data_by_cpf, cpf)

    @classmethod
    def scrape_approvals_on_page(cls, path):
        soup_content = cls.scrape_soup(path)
        cls.scrape_approvals_cpf_list(soup_content)

    @classmethod
    def initialize(cls, index):
        path = f'/approvals/{index}'
        cls.scrape_approvals_on_page(path)
