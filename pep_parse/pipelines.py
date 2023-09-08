import csv
from collections import defaultdict

from .settings import STATUS_FILE_NAME, BASE_DIR, RESULTS


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        RESULTS_DIR = BASE_DIR / RESULTS
        with open(RESULTS_DIR / STATUS_FILE_NAME,
                  mode='w',
                  encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([
                ("Статус", "Количество"),
                *self.status_counts.items(),
                ("Total", sum(self.status_counts.values()))
            ])
