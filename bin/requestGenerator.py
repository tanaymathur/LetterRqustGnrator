__author__ = 'knight'


import itertools
from jsonParamsAggregator import JsonParamsAggregator
from requestTemplate import *


# def ltr_attributes_receiver(ltr_nme , ltr_cde , ltr_variables_list):
# for L in range(0,len(ltr_variables_list)+1):
#         for subset in itertools.combinations(ltr_variables_list,L):
#             if(len(subset)>0):
#                 print(subset)

def ltr_attributes_receiver(ltr_nme, ltr_cde, ltr_variables_list):
    for L in range(len(ltr_variables_list), 0, -1):
        string = []
        obj = JsonParamsAggregator()
        for it in (range(L - 1, -1, -1)):
            # print(ltr_variables_list[it], end="")
            string.append(obj.addCurlyBraces(obj.paramsValue(ltr_variables_list[it].strip())))
        var = obj.assembleJsonString(",".join(string))
        print(obj.addCurlyBraces(var))
        # requestTemplate.request(obj.addCurlyBraces(var))


ltr_attributes_receiver('LTR1', 'BARLTR1', ['var1', 'var2', 'var3'])




