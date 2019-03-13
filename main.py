#!/usr/bin/python

import csv
import json
import math
import sys
import xml.etree.ElementTree as eTree
from xml.dom import minidom

#helper function to convert Stupidity and Courage values to True value
def trueVal(x):
    temp = x
    temp = math.atan(float(temp)) + (math.pi/2)
    temp = temp * 100 / math.pi
    return temp

def main():
    #set init variables
    count = 0
    data = []
    with open('kerbals.csv') as f:
        reader = csv.reader(f)
        
        #if XML is found on the argument line, first checks length to avoid OOB error
        if(len(sys.argv) == 2 and sys.argv[1] == 'XML'):
            root = eTree.Element("Kerbals")
            for row in reader:
                #set headers
                if(count == 0):
                    header = row
                    count = count + 1
                else:
                    #creates individual kerbal for organization in XML
                    newEl = eTree.SubElement(root, "Kerbal")
                    for i in range(0, len(row)):
                        if(header[i] == 'Courage' or header[i] == 'Stupidity'):
                            temp = trueVal(row[i])
                            eTree.SubElement(newEl, header[i]).text = str(round(temp))
                        else:
                            eTree.SubElement(newEl, header[i]).text = row[i]
            #converts to string, and indents for pretty print
            tree = eTree.tostring(root, encoding='utf8', method='xml')
            myXML = minidom.parseString(eTree.tostring(root)).toprettyxml(indent="   ")
            print(myXML)
        else:
            #iterate through each row
            for row in reader:
                x = {}
                #set headers
                if(count == 0):
                    header = row
                    count = count + 1
                else:
                    #iterate through each value in row
                    for i in range(0, len(row)):
                        #convert courage and stupidity values to true value
                        if(header[i] == 'Courage' or header[i] == 'Stupidity'):
                            temp = trueVal(row[i])
                            x[header[i]] = int(round(temp))
                        #else add header key with value to json
                        else:
                            x[header[i]] = row[i]
                    #add all row vals w/ keys to json array
                    data.append(x)
            print(json.dumps(data, indent = 2))
            
    
if __name__ == '__main__':
    main()