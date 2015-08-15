# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:17:02 2015

@author: aduba_000
"""
import Quandl
import json
import pprint


class CompanyCodes:
    def __init__(self, symbol, key):
        self.symbol = symbol;
        self.key = key;
        self.rawData = []
        self.companyAnnualCodes = {}
        self.codes = []
        #Process
        self.getDatasets()
        self.getAnnualPropertyCodes()
        self.getCodes()
    
    def addAnnualNewCode(self, key, value):
        self.companyAnnualCodes[key] = value
        
    def isName(self, name):
        s = "("+ self.symbol + ")"
        return s in name 
        
    def getDatasets(self):
        print "In get datasets"
        datasets = Quandl.search(query = self.symbol, source = "SEC", prints = False, authtoken=self.key)
        self.rawData = datasets
        
    def getAnnualPropertyCodes(self):
        print "Get Annual Property Codes"
        for i in self.rawData:
            for j in i:
                if self.isName(i['name']) and i['freq'] == 'annual' :
                    CODE = i['code']
                    self.addAnnualNewCode(i['name'], CODE)
                
                
    def printAnnualData(self):
        print "In Print Data"
        print json.dumps(self.companyAnnualCodes, indent=1)
        
    def getCodes(self):
        self.codes = self.companyAnnualCodes.values()
        
        
    

    
        
        