# -*- coding: utf-8 -*-

import ast

class Configuration:
    
    def __init__(self, config):
        self.config = config

    def getOptions(self, section):
        return self.config.options(section)
        
    def get(self, section,option):
        if self.config.has_section(section) and self.config.has_option(section,option) :
            return self.config.get(section, option)
        else:
            return None
    
    def getCollection(self, section,option):
        '''dict example: {1:'aaa',2:'bbb'}'''
        value = self.get(section, option)
        if value is not None:
            return ast.literal_eval(value)
        else:
            return value