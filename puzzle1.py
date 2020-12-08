#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:29:00 2020

@author: joanluc
"""
def addTo2020(i,j):
    if i+j==2020:
        return i*j
    else:
        return None

def listFile(finame):
    l=list()
    f=open(finame,"r")
    for n in f:
        # print(n)
        l.append(int(n))
    f.close()
    return(l)

    
l=listFile("input")    
for i in range(0,len(l)):
     n1=l[i]
     for j in range (i+1,len(l)):
         n2=l[j]
         result=addTo2020(n1,n2)
         if result != None:
             print(n1,n2,result)
             exit(result)
         
         
    
    
    
    