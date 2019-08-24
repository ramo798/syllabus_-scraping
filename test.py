import time
from concurrent.futures import ThreadPoolExecutor
from logging import StreamHandler, Formatter, INFO, getLogger
from scraping import Scraping


def init_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)


def task(v):
    getLogger().info("%s start", v)
    Scraping()
    getLogger().info("%s end", v)

def task2():
    time.sleep(1.0)


def main():
    init_logger()
    getLogger().info("main start")
    with ThreadPoolExecutor(max_workers=4, thread_name_prefix="thread") as executor:
        for i in range(4):
            executor.submit(task,i)
        getLogger().info("submit end")
    getLogger().info("main end")


if __name__ == "__main__":
    main()