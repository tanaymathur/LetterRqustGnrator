__author__ = 'knight'
import json


mandatoryParamstr =  ['letterType','ccAccntId' , 'srcSystemCode','isReconRequired']
variablesMockValue = 'atrb_value.json'

with open(variablesMockValue , 'r') as jsonIn:
    attributeValue = json.load(jsonIn)

class JsonParamsAggregator(object):
    def __init__(self):
        self.postString = ""

    @staticmethod
    def paramsValue(parameter):
        return ('"' + parameter + '" : "' + attributeValue[parameter] + '"')

    @staticmethod
    def variablesValue(variableList):
        return '"variable" : [' + variableList + ']'

    @staticmethod
    def addCurlyBraces(parameter):
        return '{'+parameter+'}'

    def assembleJsonString(self,string):
        for index in mandatoryParamstr:
           self.postString = self.postString+self.paramsValue(index)+','
        self.postString += self.variablesValue(string)
        return self.postString
