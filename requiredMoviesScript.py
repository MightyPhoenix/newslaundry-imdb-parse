# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:56:41 2020

@author: agnib
"""
import re
import csv
dataList = []
finalData = []

# PARSING REQUIRED Movies
with open('Box-office collection - Sheet2.csv','r',encoding="utf-8") as csv_file:
    for line in csv_file:
        dataList.append(line.split(","))
# HEADER CLEANUP
dataList.pop(0)

# CLEANUP
for data in dataList:
    data[1] = re.sub("\n", "", data[1])
    
totalRequiredCount = len(dataList)
    
    
count=1
with open('title.basics.csv','r',encoding="utf-8") as title_db:
    for line in title_db:
        movieList = line.split(",")
        for data in dataList:
            if(data[1]==movieList[2] and data[0]==movieList[5] and movieList[1]=='movie'):
                with open('title.akas.tsv','r',encoding="utf-8") as akas_db:
                    for line in akas_db:
                        akas_data = line.split(",")
                        if(akas_data[0]==movieList[0] and akas_data[3]=='IN'):
                            if [movieList[0],movieList[2],movieList[5]] in finalData:
                                continue
                            else:
                                finalData.append([movieList[0],movieList[2],movieList[5]])
                                print("Found "+str(count)+"/"+str(totalRequiredCount))
                                count+=1
                                continue

# Remove Duplicates
# finalData2 = list(set(tuple(sorted(sub)) for sub in finalData))  


# Write in CSV 
with open('requiredMoviesFound.csv','w',encoding="utf-8") as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(["tconst","title","year"])
        csvwriter.writerows(finalData)
    
print(len(finalData))