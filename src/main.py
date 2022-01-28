from scrapers.approvals_scraper import ApprovalsScraper
from database.models.approvals_model import ApprovalsModel


class Main:
    collected_approvals = []

    @classmethod
    def run_approvals_scraper(cls):
        approvals_scraper = ApprovalsScraper()
        approvals_scraper.scrape_approvals_all_pages()
        cls.collected_approvals = approvals_scraper.approvals_data

    @classmethod
    def save_collected_approvals(cls):
        for approval in cls.collected_approvals:
            ApprovalsModel.insert_approval(approval['cpf'], approval['name'], approval['score'])


if __name__ == '__main__':
    Main.run_approvals_scraper()
    Main.save_collected_approvals()
