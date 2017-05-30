import csv

from requestGenerator import ltr_attributes_receiver


inputCsv = 'ltr_codes.csv'




with open(inputCsv, 'r') as fin :
    reader = csv.DictReader(fin, delimiter=',')
    for line in (reader):
        # ltrName =  line[1][]
        ltrEvent = line['LTR_EVENT']
        ltrCode =  line['LTR_CODE']
        if(line['Variables'] !=''):
            ltrVariables = line['Variables'].split(',')
            if  len(ltrVariables):
                print("There",ltrEvent,ltrCode,ltrVariables)
                ltr_attributes_receiver(ltrEvent,ltrCode,ltrVariables)
                # print(ltrVariables , variable_value)

