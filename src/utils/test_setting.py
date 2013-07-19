# -*- coding: utf-8 -*-
from utils.setting import Configuration
import os, ConfigParser

class TestConfiguration(Configuration):
    def __init__(self):
        Configuration.__init__(self, ConfigParser.ConfigParser())
        current_directory = os.path.dirname(os.path.abspath(__file__))
        etc_directory = os.path.join(current_directory, '../../etc')
        ini_file_path = os.path.join(etc_directory,'test_config.ini')
        self.config.read(ini_file_path)
        
configuration=TestConfiguration()