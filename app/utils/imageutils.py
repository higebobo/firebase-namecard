# -*- mode: python -*- -*- coding: utf-8 -*-
import io
import os

from PIL import Image


def resize(filepath, size=0, quality=50, limit_size=100000, format='PNG', optimize=True):
    img = Image.open(filepath)
    obj = io.BytesIO()
    if size != 0  and max(img.size) > size:
        img.thumbnail((size, size))
    file_size = os.path.getsize(filepath)

    if file_size > limit_size:
        img.save(obj, format=format, quality=quality, optimize=True)
    else:
        img.save(obj, format=format)

    result = obj.getvalue()
    obj.close()

    return result
