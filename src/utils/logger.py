# -*- coding: utf-8 -*-

import logging.config, os

class Logger:
    '''Configuration file Loader'''
    
    def __init__(self):
        #File config
        current_directory = os.path.dirname(os.path.abspath(__file__))
        base_directory = os.path.join(current_directory, '..')
        log_config_path = os.path.join(base_directory, 'logging.conf')
        logging.config.fileConfig(log_config_path)
        
    def getLogger(self, name):
        return logging.getLogger(name)
logger=Logger().getLogger('[task]')

def test():
    logger = Logger().getLogger("Logger test")
    logger.debug("1")
    logger.info("2")
    logger.warn("3")
    logger.error("4")
    logger.critical("5")
    
if __name__ == "__main__":test()