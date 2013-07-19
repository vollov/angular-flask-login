# -*- coding: utf-8 -*-

import unittest
from utils.prod_setting import configuration

class ProdSettingUT(unittest.TestCase):
    
    def testDict(self):
        expected = {'INV_DMO_ClientInformation_EJBClient':\
         'InvestmentServices', 'INV_DMO_AccountInformation_EJBClient': \
         'InvestmentServices'}
        actual = configuration.getCollection('IntelligentForms','other_project')

#         print configuration.getCollection('IntelligentForms','other_project')
        self.assertEqual(expected,actual,'dict setting not match')
        
if __name__ == "__main__":
    unittest.main()