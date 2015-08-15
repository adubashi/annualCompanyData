# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 22:29:26 2015

@author: aduba_000
"""
import CompanyCodes
import Quandl
import json



class companyAnnualData:
    def __init__(self, symbol, key):
        self.symbol = symbol
        self.key = key
        self.companyCodes  = CompanyCodes.CompanyCodes(symbol,key)
        self.annualData = {}
    
    def getPropData(self, prop):
        value = Quandl.get(prop, authtoken=self.key)
        return float(value.iloc[0])
        
    def getAnnualData(self):
        for i in self.companyCodes.codes:
            value = self.getPropData(i)
            self.annualData[i] = value;
    
    def printAnnualData(self):
        print json.dumps(self.annualData, indent=1)
    
    def exportToJSON(self):
        with open('result.json', 'w') as fp:
            json.dump(self.annualData, fp)
        