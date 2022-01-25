# -*- mode: python -*- -*- coding: utf-8 -*-
from app import config
from .firebase import Firebase

firebase_instance = Firebase(
    service_account_key=config.FIREBASE_SERVICE_ACCOUNT_KEY,
    app_url=config.FIREBASE_APP_URL,
    collection=config.FIREBASE_COLLECTION
)
