#coding=utf-8
'''
Created on 2015年10月14日

@author: gepeng
'''
import unittest
import MySQLdb
from LoadCase.CaseFolderParser import CaseFolderParser

from json import *
import requests
from symbol import parameters
from json.decoder import JSONDecoder


class ServiceInterfaceCaseTest(unittest.TestCase):


    
    
    def setUp(self):
        folderpath = 'C:\Users\gepeng\workspace\ZTEST\Case\demo'
        self.config = CaseFolderParser(folderpath)

    def test_execute(self):
        inPut = self.config.getInPut()
        expect = self.config.getExpect()

        print expect
        
        d = JSONDecoder()
        data = d.decode(inPut.get('parameters'))
       
        if inPut.get('method')=='POST':
            r = requests.post(inPut.get('url'), data)
        else:
            r = requests.get(inPut.get('url'), parameters=data)
        
        response = d.decode(str(r.text))
        expectResponse = d.decode(expect.get('response'))
    
        print expect.get('sql')
        expectSql = d.decode(expect.get('sql'))
        print expectSql
        expectSqlQuery = expectSql.get('query')
        expectSqlResult = tuple(expectSql.get('result').encode(encoding='UTF-8',errors='strict').split(','))

        conn = MySQLdb.connect(host='172.18.33.37', user='root', passwd='123456', db='meshare', port=3306)
        cur=conn.cursor()
        cur.execute(expectSqlQuery)
        result = cur.fetchone()

        
        self.assertTupleEqual(result, expectSqlResult)
        self.assertDictContainsSubset(expectResponse, response)
        
        
        
    
    def tearDown(self):
        pass
        





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()