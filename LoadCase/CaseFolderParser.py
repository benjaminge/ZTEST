#coding=utf-8
'''
Created on 2015年10月14日

@author: gepeng
'''
import ConfigParser

class CaseFolderParser():
    '''
    classdocs
    '''
    def __init__(self,folderpath):
        self.config = ConfigParser.ConfigParser()
        f = open(folderpath+'\caseinfo.properties',"r")
        self.config.readfp(f)

    def getSetUp(self):
        '''
        Constructor
        '''
        pass
    
 
    def getInPut(self):
        inPut = {}
        inPut['url'] = self.config.get("INPUT", "URL")
        inPut['method'] = self.config.get("INPUT", "METHOD")
        inPut['parameters'] = self.config.get("INPUT", "PARAMETERS")
        return inPut
    

    def getTearDown(self):
        pass
    

    def getExpect(self):
        expect = {}
        expect['response'] = self.config.get("EXPECT", "RESPONSE")
        expect['sql'] = self.config.get("EXPECT", "SQL")
        return expect
        
        