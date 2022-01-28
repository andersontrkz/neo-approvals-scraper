from mimetypes import init
from scrapers.approvals_scraper import ApprovalsScraper
from database.models.approvals_model import ApprovalsModel
import sys

# BASED ON
# https://stackoverflow.com/questions/6809402/python-maximum-recursion-depth-exceeded-while-calling-a-python-object

sys.setrecursionlimit(12000)


class Main:
    @classmethod
    def run_approvals_scraper(cls):
        ApprovalsModel.initialize()
        ApprovalsScraper.initialize_runtime()


if __name__ == '__main__':
    Main.run_approvals_scraper()
