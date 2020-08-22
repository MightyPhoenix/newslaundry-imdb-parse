# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:05:44 2020

@author: agnib
"""
import csv
import re
requiredMovies = []
moviesWithActors = []
dataSet1 = []

# [TCONST,TITLE,YEAR]
with open('requiredMoviesFound.csv','r',encoding="utf-8") as rmov_file:
    for line in rmov_file:
        data = line.split(",")
        data[2] = re.sub("\n", "", data[2])
        requiredMovies.append(data)
requiredMovies.pop(0)

#[TCONST,TITLE,YEAR,ORDER,NCONST,CHAR]
count = 1
with open('CSV files/title.principals.csv','r',encoding="utf-8") as movie_princ:
    for movie in movie_princ:
        data = movie.split(",")
        for reqM in requiredMovies:
            if((data[0]==reqM[0]) and (data[3]=='actor' or data[3]=='actress')):
                moviesWithActors.append([data[0],reqM[1],reqM[2],data[1],data[2],data[5]])
                print("Found ",count,'/599')
                count+=1
         
#[TCONST,TITLE,YEAR,ORDER,ACTORNAME,CHAR]
print("Adding Names")
count = 0 
with open('CSV files/name.basics.csv','r',encoding="utf-8") as name_db:
    for line in name_db:
        data=line.split(",")
        for movie in moviesWithActors:
            if(movie[4]==data[0]):
                dataSet1.append([movie[0],movie[1],movie[2],movie[3],data[1],movie[5]])
                print("Adding ",count," name")
                count+=1

# Write in CSV 
print("Writing file")
with open('dataset1.csv','w',encoding="utf-8") as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(["tconst","title","year","ordering","Actor","Character Played"])
        csvwriter.writerows(dataSet1)
print("ok",len(dataSet1))