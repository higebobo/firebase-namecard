# -*- mode: python -*- -*- coding: utf-8 -*-
import os
from pathlib import Path

from dotenv import load_dotenv

APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = Path(APP_DIR).parent

dotenv_path = os.path.join(PROJECT_DIR, '.env')
load_dotenv(dotenv_path)

# general
PROJECT_NAME = 'namecard'
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
IMAGE_DIR = os.path.join(DATA_DIR, 'image')
LOG_DIR = os.path.join(PROJECT_DIR, 'log')
try:
    WAIT = int(os.getenv('WAIT'))
except:
    WAIT = 3

# data
#DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
CSV_PATH = os.path.join(DATA_DIR, os.getenv('CSV_FILE', 'data.csv'))

# image
try:
    IMAGE_SIZE = int(os.getenv('IMAGE_SIZE'))
except:
    IMAGE_SIZE = 640
try:
    IMAGE_LIMIT_SIZE = int(os.getenv('IMAGE_LIMIT_SIZE'))
except:
    IMAGE_LIMMIT_SIZE = 500000
try:
    IMAGE_QUOLITY = int(os.getenv('IMAGE_QUOLITY'))
except:
    IMAGE_QUOLITY = 20

# log
DEBUG_LOG = os.path.join(LOG_DIR, 'debug.log')
ERROR_LOG = os.path.join(LOG_DIR, 'error.log')
LOG_MAX_BYTE = int(os.getenv('LOG_MAX_BYTE', '100000'))
LOG_BACKUP_COUNT = int(os.getenv('LOG_BACKUP_COUNT', '10'))

# firebase
FIREBASE_PROJECT_ID = os.getenv('FIREBASE_PROJECT_ID', '')
FIREBASE_SERVICE_ACCOUNT_KEY = {
    'type': 'service_account',
    'project_id': FIREBASE_PROJECT_ID,
    'private_key': os.getenv('FIREBASE_PRIVATE_KEY', '').replace('\\n', '\n'),
    'client_email': os.getenv('FIREBASE_CLIENT_EMAIL', ''),
    'token_uri': os.getenv('FIREBASE_TOKEN_URI', '')
}
FIREBASE_APP_URL = f'{FIREBASE_PROJECT_ID}.appspot.com'
FIREBASE_COLLECTION = os.getenv('FIREBASE_COLLECTION', '')
