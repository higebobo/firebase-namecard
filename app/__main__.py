# -*- mode: python -*- -*- coding: utf-8 -*-
import argparse
import os
import time

from app import config
from app.service.logger import Logger
from app.service.net import firebase_instance as firebase
from app.utils.textutils import MediaReader
from app.utils.imageutils import resize


def check_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', choices=['insert'], help='mode')
    parser.add_argument('-r', '--resize', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')

    return parser.parse_args()


def main():
    # arguments
    args = check_args()

    # logging
    log = Logger(
        app_name=config.PROJECT_NAME,
        debug_log=config.DEBUG_LOG,
        error_log=config.ERROR_LOG,
        max_byte=config.LOG_MAX_BYTE,
        backup_count=config.LOG_BACKUP_COUNT
    )
    logger = log.logger

    # main procedure
    if args.mode == 'insert':
        reader = MediaReader()
        data = reader.parse(config.CSV_PATH)
        for x in data:
            oid = x.get('id')
            # insert document into collection
            result = firebase.insert_document(oid=oid, data=x)
            status = result.get('status')
            message = result.get('message')
            if status == 'ok':
                logger.info(message)
            else:
                logger.fatal(message)
            if args.verbose:
                print(message)
            # check image file
            filepath = os.path.join(config.IMAGE_DIR, oid)
            if not os.path.exists(filepath):
                if args.verbose:
                    print(f'{filepath} not found')
                    continue
            # insert image
            if args.resize:
                contents = resize(filepath, config.IMAGE_SIZE, config.IMAGE_QUOLITY, config.IMAGE_LIMIT_SIZE)
                result = firebase.insert_image_from_string(oid, contents)
            else:
                result = firebase.insert_image_from_filename(oid, filepath)
            if status == 'ok':
                logger.info(message)
            elif status == 'ng':
                logger.fatal(message)
            if args.verbose:
                print(message)
                            
            time.sleep(config.WAIT)

if __name__ == "__main__":
    main()
