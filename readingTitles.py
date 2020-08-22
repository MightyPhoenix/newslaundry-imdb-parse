# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:47:08 2020

@author: agnib
"""
import re
count = 0 

movies = []
movies2 = []

with open('requiredMoviesFound.csv','r',encoding="utf-8") as csv_file:
    for line in csv_file:
        data = line.split(",")
        data[2] = re.sub("\n","",data[2])
        movies.append(data)

with open('dataset3.csv','r',encoding="utf-8") as ds_3:
    for line in ds_3:
        data = line.split(",")
        movies2.append([data[0],data[1],data[2]])

print(len(movies2))
        
for movie in movies:
    if(movie in movies2):
        continue
    else:
        print(movie)

print(len(movies))
        

    