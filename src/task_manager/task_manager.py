import threading
from queue import Queue

from task_manager.buffer import Buffer

# https://stackoverflow.com/questions/45920583/in-python-whats-the-cleanest-way-to-read-from-a-queue-while-its-not-empty-an


class TaskManager:
    def __init__(self, task) -> None:
        self.task = task

    task = ''
    jobs = Queue()
    max_threads = 49

    def execute_task(self, arg):
        self.task(arg)

    def initialize(self):
        start = 1
        final = 4673

        for page in range(start, final):
            action = [self.execute_task, page]
            self.jobs.put(action)

        for i in range(self.max_threads):
            worker = threading.Thread(target=self.do_stuff, args=(self.jobs,))
            worker.start()

        self.jobs.join()

    @classmethod
    def queue_rows(cls, q, block=False, timeout=None):
        while not q.empty():
            with Buffer(q, block, timeout) as row:
                yield row

    @classmethod
    def do_stuff(cls, q):
        for row in cls.queue_rows(q):
            row[0](row[1])
