#!/bin/python
#coding=utf-8
'''
Created on 2016年3月21日

@author: wujianxin
'''
import unittest
class ATestCase(unittest.TestCase):
    def setUp(self):
        print("Set up Testcase!")
    def tearDown(self):
        print("Tear down Testcase!")
        
    def testAdd(self):
        '''查看加法是否正确'''
        self.assertEqual(1+1, 1, 'add wrong')
        
    def testMinus(self):
        '''查看减法是否正确'''
        self.assertEqual(5-2, 3, 'Minus wrong')
            
def ASuite():
    ASuite = unittest.TestSuite()
    ASuite.addTest(ATestCase('testAdd'))            
    ASuite.addTest(ATestCase('testMinus'))
    return ASuite
    
runner = unittest.TextTestRunner()
runner.run(ASuite())
                
# if __name__ == '__main__':
# unittest.main()
