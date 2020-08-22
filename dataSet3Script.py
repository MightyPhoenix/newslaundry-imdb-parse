# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:47:00 2020

@author: agnib
"""
import csv
import re
count = 1 
requiredMovies = []
dataSet_nconst = []
dataSet_nconst2 = []
dataset3 = []

# [TCONST,TITLE,YEAR]
with open('requiredMoviesFound.csv','r',encoding="utf-8") as rmov_file:
    for line in rmov_file:
        data = line.split(",")
        data[2] = re.sub("\n", "", data[2])
        requiredMovies.append(data)
requiredMovies.pop(0)

# [TCONST,TITLE,YEAR,nconst,nconst] = dataSet_nconst
with open('CSV files/title.crew.csv','r',encoding="utf-8") as csv_file:
    for line in csv_file:
        data = line.split(",")
        for mov in requiredMovies:
            # Cleanup
            if(data[0]==mov[0]):
                dataSet_nconst.append([mov[0],mov[1],mov[2],data[1],data[2]])
                print("Found ",count)
                count+=1
# CLEANUP
for movie in dataSet_nconst:
    movie[3] = re.sub("\n","",movie[3])
    movie[3] = re.sub('"','',movie[3])
    movie[4] = re.sub("\n","",movie[4])
    movie[4] = re.sub('"','',movie[4])
          
# [TCONST,TITLE,YEAR,DIRECTOR,nconst]
print("Searching for Directors")
with open('CSV files/name.basics.csv','r',encoding="utf-8") as name_db:
    for line in name_db:
        data = line.split(",")
        for movie in dataSet_nconst:
            if(data[0]==movie[3]):
                dataSet_nconst2.append([movie[0],movie[1],movie[2],data[1],movie[4]])
                
# [TCONST,TITLE,YEAR,DIRECTOR,WRITER]
print("Searching for Writers")
with open('CSV files/name.basics.csv','r',encoding="utf-8") as name_db:
    for line in name_db:
        data = line.split(",")
        for movie in dataSet_nconst2:
            if(data[0]==movie[4]):
                dataset3.append([movie[0],movie[1],movie[2],movie[3],data[1]])
        
# Write in CSV 
print("Writing file")
with open('dataset3.csv','w',encoding="utf-8") as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(["tconst","title","year","director(s)","writer(s)"])
        csvwriter.writerows(dataset3)

        
# print(requiredMovies)