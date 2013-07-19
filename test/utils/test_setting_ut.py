# -*- coding: utf-8 -*-

import unittest
from utils.test_setting import configuration

class TestSettingUT(unittest.TestCase):
    
    def testDict(self):
        expected = ['SQL Scripts', 'XML', 'PDF']
        actual = configuration.getCollection('sql','file_type_list')
#         print configuration.getCollection('sql','file_type_list')
        self.assertEqual(expected,actual,'dict setting not match')
        
if __name__ == "__main__":
    unittest.main()