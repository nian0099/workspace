# -*- coding:utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler
from src.utils.config import LOG_PATH


class Logger(object):
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'test_error.log'
        self.backup_count = 5
        #日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'
