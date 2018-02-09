# -*- coding:utf-8 -*-

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from src.utils.config import LOG_PATH,Config


class Logger(object):
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = Config().get('log')

        #日志文件名称
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else 'test.log'
        #日志保留个数
        self.backup_count = c.get('backup_count') if c and c.get('backup_count') else 5
        #日志输出级别
        self.console_output_level = c.get('output_level') if c and c.get('output_level') else 'WARNING'
        self.file_output_level = c.get('file_level') if c and  c.get('file_level') else 'DEBUG'
        #日志输出格式
        pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers: #避免重复日志
            # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH,self.log_file_name),
                                                    when='D',  #时间单位
                                                   interval= 1,  #单位时间
                                                   backupCount=self.backup_count,  #本地日志个数
                                                   delay=True,  #延迟写入，	如果设置为True那么只有调用了emit()后才会写入文件
                                                   utc=True,  #设置为False(默认)使用本地时间，否则使用标准时间
                                                   encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()



