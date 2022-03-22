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

    """
    [Alternative to async initialize example]
    import asyncio
    import nest_asyncio
    import concurrent.futures

    async def async_initialize(cls, index):
        print(f'initialize {index}')
        nest_asyncio.apply()

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:

            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(
                    executor,
                    cls.fetch,
                    cls.base_url + '/approvals/' + str(index),
                    # print(cls.base_url + '/approvals/' + str(index))
                )
            ]
            for response in await asyncio.gather(*futures):
                # print(f'Scrapping approval page {response.request.path_url}')
                print(f'{response} | {str(index)}')
                cls.scrape_approvals_on_page(response.text, loop)
    """

    """
    [Alternative to async scrape_approvals_cpf_list example]
    async def scrape_approvals_cpf_list(cls, soup_content):
        # print('scrape_approvals_cpf_list')
        cpf_elements = cls.scrape_getall_children(soup_content, 'li', 'a')
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:

            loop = asyncio.get_event_loop()
            futures = [
                loop.run_in_executor(
                    executor,
                    cls.fetch,
                    cls.base_url + '/candidate/' + str(cpf_element.string),
                    # "print(f'Scrapping cpf {cpf_element.string}')"
                )
                for cpf_element in cpf_elements
            ]
            for response in await asyncio.gather(*futures):
                cpf = response.request.path_url.split('/candidate/')[1]
                soup = cls.scrape_soup(response.text)
                # print('scrape_approvals_cpf_list')
                # print(f'{threading.active_count()}')
                cls.scrape_approval_data_by_cpf(cpf, soup)
      """
