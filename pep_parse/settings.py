from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

PEP_FILE_NAME = 'pep_%(time)s.csv'
STATUS_TIME = datetime.strftime(datetime.now(), '%Y-%m-%dT%H-%M-%S')
STATUS_FILE_NAME = f'status_summary_{STATUS_TIME}.csv'

FEEDS = {
    f'{RESULTS}/{PEP_FILE_NAME}': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}