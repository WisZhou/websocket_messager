#!/usr/bin/env python
# coding: utf-8

import logging

import config


def get_common_logger(name='common', logfile=None):
    '''
    args: name (str): logger name
        logfile (str): log file, use stream handler (stdout) as default.
    return:
        logger obj
    '''
    my_logger = logging.getLogger(name)
    my_logger.setLevel(config.LOG_LEVEL)
    if logfile:
        handler = logging.FileHandler(logfile)
    else:
        handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(formatter)
    my_logger.addHandler(handler)
    # Stop logger propagate, forbiden duplicate log.
    my_logger.propagate = False
    return my_logger


COMMON_LOGGER = get_common_logger('common logger')

if __name__ == '__main__':
    COMMON_LOGGER.debug('test')
