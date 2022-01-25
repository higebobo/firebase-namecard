# -*- mode: python -*- -*- coding: utf-8 -*-
import os
import time

from google.cloud import storage
from google.oauth2 import service_account
import firebase_admin
from firebase_admin import (credentials, firestore)


class Firebase(object):
    def __init__(self, service_account_key, app_url, collection):
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

    def insert_document(self, oid, data):
        try:
            self.ref.document(oid).set(data)
            message = f'add {oid} into collection'
            result = {'status': 'ok', 'message': message}
        except Exception as e:
            message = str(e)
            result = {'status': 'ng', 'message': message}

        return result

    def delete_document(self, oid):
        try:
            self.ref.document(oid).delete
            message = f'delete {oid} from collection'
            result = {'status': 'ok', 'message': message}
        except Exception as e:
            message = str(e)
            result = {'status': 'ng', 'message': message}

        return result

    def insert_image_from_filename(self, oid, filepath, overwrite_image=False):
        blob = self.bucket.blob(oid)
        if not overwrite_image:
            if blob.exists():
                return {'message': f'{oid} exists'}
        try:
            blob.upload_from_filename(filepath)
            return {'status': 'ok', 'message': f'upload {oid}'}
        except Exception as e:
            return {'status': 'ng', 'message': str(e)}

    def insert_image_from_string(self, oid, contents, overwrite_image=False):
        blob = self.bucket.blob(oid)
        if not overwrite_image:
            if blob.exists():
                return {'message': f'{oid} exists'}
        try:
            blob.upload_from_string(contents, content_type='image/png')
            return {'status': 'ok', 'message': f'upload {oid}'}
        except Exception as e:
            return {'status': 'ng', 'message': str(e)}
