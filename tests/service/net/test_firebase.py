# -*- mode: python -*- -*- coding: utf-8 -*-
import datetime
import pytest

from app.service.net import firebase_instance as firebase

@pytest.fixture
def fb():
    return firebase


@pytest.mark.firebase
def test(fb):
    assert fb

@pytest.mark.firebase
def test_insert_document(fb):
    oid = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    data = {'name': 'test'}
    result = fb.insert_document(oid=oid, data=data)

    assert result.get('status') == 'ok'

    result = fb.delete_document(oid=oid)

    assert result.get('status') == 'ok'
