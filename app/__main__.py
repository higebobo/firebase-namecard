# -*- mode: python -*- -*- coding: utf-8 -*-
import argparse

from app import config
from app.service.logger import Logger
from app.service.net.firebase import Firebase
from app.utils.textutils import MediaReader


def check_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', choices=['insert'], help='mode')
    parser.add_argument('-v', '--verbose', action='store_true')

    return parser.parse_args()


def main():
    args = check_args()

    log = Logger(app_name=config.PROJECT_NAME, debug_log=config.DEBUG_LOG,
                 error_log=config.ERROR_LOG, max_byte=config.LOG_MAX_BYTE,
                 backup_count=config.LOG_BACKUP_COUNT)
    logger = log.logger
    firebase = Firebase(
        service_account_key=config.FIREBASE_SERVICE_ACCOUNT_KEY,
        app_url=config.FIREBASE_APP_URL,
        collection=config.FIREBASE_COLLECTION,
        logger=logger
    )
    if args.mode == 'insert':
        reader = MediaReader()
        data = reader.parse(config.CSV_PATH)
        firebase.insert(data=data, image_dir=config.IMAGE_DIR, verbose=args.verbose)


if __name__ == "__main__":
    main()
