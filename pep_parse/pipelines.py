import csv
from collections import defaultdict
from itemadapter import ItemAdapter

from .settings import RESULTS_DIR, STATUS_FILE_NAME, BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('status'):
            pep_status = adapter['status']
            self.status_counts[pep_status] += 1
        return item

    def close_spider(self, spider):
        status_counts = self.status_counts
        total_count = sum(status_counts.values())
        with open(RESULTS_DIR / STATUS_FILE_NAME,
                  mode='w',
                  encoding='utf-8') as csvfile:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for status, count in status_counts.items():
                writer.writerow({'Статус': status, 'Количество': count})
            writer.writerow({'Статус': 'Total', 'Количество': total_count})
