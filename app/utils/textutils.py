# -*- mode: python -*- -*- coding: utf-8 -*-
import csv

import mojimoji


class CsvReader(object):
    def __init__(self):
        self.encoding = 'utf8'
        self.newline = ''


class MediaReader(CsvReader):
    def __init__(self):
        super().__init__()

    def parse(self, filepath, skip_title=True):
        with open(filepath, encoding=self.encoding, newline=self.newline) as f:
            reader = csv.reader(f)
            if skip_title:
                reader.__next__()
            for row in reader:
                data = {
                    'lastname': row[0],
                    'fastname': row[1],
                    'lastname-kana': mojimoji.han_to_zen(row[2]),
                    'fastname-kana': mojimoji.han_to_zen(row[3]),
                    'company': row[4],
                    'company-kaka': mojimoji.han_to_zen(row[5]),
                    'department': row[6],
                    'job-title': row[7],
                    'zip-code': row[9],
                    'prefecture': row[11],
                    'city': row[12],
                    'address1': row[13],
                    'address2': row[14],
                    'tel1': row[16],
                    'tel2': row[17],
                    'mobile': row[19],
                    'mail': row[21],
                    'id': row[66].split('\\')[-1]
                    # 'fore': row[66],
                    # 'back': row[65]
                }
                yield data
