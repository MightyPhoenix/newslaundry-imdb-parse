# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:34:34 2020

@author: agnib
"""
import csv
import re
requiredMovies = []
moviesWithJob = []
dataSet2 = []

# [TCONST,TITLE,YEAR]
with open('requiredMoviesFound.csv','r',encoding="utf-8") as rmov_file:
    for line in rmov_file:
        data = line.split(",")
        data[2] = re.sub("\n", "", data[2])
        requiredMovies.append(data)
requiredMovies.pop(0)

#[TCONST,TITLE,YEAR,ORDER,NCONST,category,job]
count = 1
with open('CSV files/title.principals.csv','r',encoding="utf-8") as movie_princ:
    for movie in movie_princ:
        data = movie.split(",")
        for reqM in requiredMovies:
            if(data[0]==reqM[0]):
                moviesWithJob.append([data[0],reqM[1],reqM[2],data[1],data[2],data[3],data[4]])
                print("Found ",count,'/1495')
                count+=1

#[TCONST,TITLE,YEAR,ORDER,NAME,category,job]
print("Adding Names")
count = 1
with open('CSV files/name.basics.csv','r',encoding="utf-8") as name_db:
    for line in name_db:
        data=line.split(",")
        for movie in moviesWithJob:
            if(movie[4]==data[0]):
                dataSet2.append([movie[0],movie[1],movie[2],movie[3],data[1],movie[5],movie[6]])
                print("Adding ",count," name")
                count+=1
                

# Write in CSV 
print("Writing file")
with open('dataset2.csv','w',encoding="utf-8") as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(["tconst","title","year","ordering","Actor","Category","Job"])
        csvwriter.writerows(dataSet2)
print("ok",len(dataSet2))   