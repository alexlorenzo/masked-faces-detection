"""
Contains all configurations for the projectself.
Should NOT contain any secrets.

>>> import settings
>>> settings.DATA_DIR
/Users/benjaminhabert/Documents/20170509_TaskForceDataEngineering_TemplateCode/data
"""
import os
import logging

# By default the data is stored in this repository's "data/" folder.
# You can change it in your own settings file.
REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
DATA_DIR = os.path.join(REPO_DIR, 'data')

DATABASE_INFOS = {
    'host': 'pyox1k01',
    'port': 1521,
    'service_name': 'EDW00_PP2',
    'username': 'EDW_ANA',
    'password': os.environ.get('DATABASE_PASSWORD'),  # this was loaded by load_dotenv
    'default_schema': 'EDW_QUA',
}


# Logging
LOGGING_FORMAT = '[%(asctime)s][%(levelname)s][%(module)s] %(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOGGING_LEVEL = logging.DEBUG
logging.basicConfig(
    format=LOGGING_FORMAT,
    datefmt=LOGGING_DATE_FORMAT,
    level=LOGGING_LEVEL
)
