# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:16:10 2020

@author: agnib
"""
import re

with open('TSV files/title.akas.tsv','r',encoding="utf-8") as tsv_file:
    print("File Read")
    with open('title.akas.tsv','w',encoding="utf-8") as csv_file:
        for line in tsv_file:
            fileContent = re.sub("\t",",",line)
            csv_file.write(fileContent)

print("Done Parsing to TSV to CSV")