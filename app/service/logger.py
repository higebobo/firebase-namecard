# -*- mode: python -*- -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler


class Logger(object):
    def __init__(self, app_name, debug_log, error_log, max_byte, backup_count):
        self.set_logger(app_name, debug_log, error_log, max_byte, backup_count)

    def set_logger(self, app_name, debug_log, error_log, max_byte, backup_count):
        self.logger = logging.getLogger(app_name)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        ## debug log (file handler)
        debug_file_handler = RotatingFileHandler(debug_log, maxBytes=max_byte,
                                                 backupCount=backup_count)
        debug_file_handler.setLevel(logging.INFO)
        debug_file_handler.setFormatter(formatter)
        self.logger.addHandler(debug_file_handler)
        ## error log (file handler)
        error_file_handler = RotatingFileHandler(error_log, maxBytes=max_byte,
                                                 backupCount=backup_count)
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(formatter)
        self.logger.addHandler(error_file_handler)
        # set default level
        self.logger.setLevel(logging.DEBUG)
