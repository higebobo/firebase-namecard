# -*- mode: python -*- -*- coding: utf-8 -*-
import os

from google.cloud import storage
from google.oauth2 import service_account
import firebase_admin
from firebase_admin import (credentials, firestore)


class Firebase(object):
    def __init__(self, service_account_key, app_url, collection, logger):
        if not (len(firebase_admin._apps)):
            cred = credentials.Certificate(service_account_key)
            firebase_admin.initialize_app(cred)
        # firestore
        db = firestore.client()
        self.ref = db.collection(collection)
        # storage
        gauth_cred = service_account.Credentials.from_service_account_info(
            service_account_key)
        client = storage.Client(credentials=gauth_cred)
        self.bucket = client.get_bucket(app_url)
        self.logger = logger

    def insert(self, data, image_dir, overwrite_image=False,
               by_filepath=False, verbose=False):
        for x in data:
            uid = x['id']

            # insert or update document
            try:
                self.ref.document(uid).set(x)
                message = f'add {uid} into collection'
                self.logger.info(message)
                if verbose:
                    print(message)
            except Exception as e:
                message = str(e)
                self.logger.fatal(message)
                if verbose:
                    print(message)

            filepath = os.path.join(image_dir, uid)
            if not os.path.exists(filepath):
                if verbose:
                    print(f'{filepath} not found')
                    continue

                blob = self.bucket.blob(uid)
                if not overwrite_image:
                    if blob.exists():
                        if verbose:
                            print(f'{uid}.png exists')
                        continue

                try:
                    if by_filepath:
                        blob.upload_from_filename()
                    else:
                        img = Image.open(filepath)
                        obj = io.BytesIO()
                        img.thumbnail((config.IMAGE_SIZE, config.IMAGE_SIZE))
                        size = os.path.getsize(filepath)

                        if size > config.IMAGE_BIGGER_SIZE:
                            img.save(obj, format='PNG',
                                     quality=config.IMAGE_QUOLITY, optimize=True)
                        else:
                            img.save(obj, format='PNG')

                        contents = obj.getvalue()
                        obj.close()

                        # upload
                        blob.upload_from_string(contents, content_type='image/png')
                        print(f'upload {uid}')

                        time.sleep(config.WAIT)


                except Exception as e:
                    pass
