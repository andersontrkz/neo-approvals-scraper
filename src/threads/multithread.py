from threading import Thread
import threading

# BASED ON
# https://docs.python.org/3/library/threading.html


class Multithread:
    @classmethod
    def initialize(cls, func, param):
        Thread(target=func, args=(param,)).start()

    @classmethod
    def initialize_args(cls, func):
        Thread(target=func).start()

    @classmethod
    def active_threads(cls):
        return threading.active_count()
