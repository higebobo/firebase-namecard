# -*- mode: python -*- -*- coding: utf-8 -*-
import json
import os

import pytest

from app import config


@pytest.fixture(scope='session', autouse=True)
def cmdopt(request):
    set_environment()


def set_environment(filename='env.json'):
    env_file = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), filename)
    if os.path.exists(env_file):
        with open(env_file) as f:
            for key, value in json.load(f).items():
                os.environ[key] = value


@pytest.fixture(scope='session', autouse=True)
def env():
    return {}
