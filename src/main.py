import time

from scrapers.approvals_scraper import ApprovalsScraper
from database.models.approvals_model import ApprovalsModel
from task_manager.task_manager import TaskManager
from threads.multithread import Multithread

# BASED ON
# https://stackoverflow.com/questions/6809402/python-maximum-recursion-depth-exceeded-while-calling-a-python-object


if __name__ == '__main__':
    t0 = time.time()

    scrapper = ApprovalsScraper()

    TaskManager(scrapper.initialize).initialize()

    print("Running async jobs...")
    while Multithread().active_threads() > 0:
        if Multithread().active_threads() < 2:
            t1 = time.time()
            length = len(scrapper.approvals_list)
            print(f"{t1-t0} seconds to download {length} approvals")
            print('Saving approvals...')
            ApprovalsModel.insert_approvals(scrapper.approvals_list)
            break
