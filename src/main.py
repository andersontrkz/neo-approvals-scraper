from scrapers.approvals_scraper import ApprovalsScraper
from database.models.approvals_model import ApprovalsModel


class Main:
    collected_approvals = []

    @classmethod
    def run_approvals_scraper(self):
        approvals_scraper = ApprovalsScraper()
        approvals_scraper.scrape_approvals_all_pages()
        self.collected_approvals = approvals_scraper.approvals_data

    @classmethod
    def save_collected_approvals(self):
        for approval in self.collected_approvals:
            ApprovalsModel.insert_approval(approval['cpf'], approval['name'], approval['score'])


if __name__ == '__main__':
    Main.run_approvals_scraper()
    Main.save_collected_approvals()
