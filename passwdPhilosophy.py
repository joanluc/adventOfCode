#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 00:03:28 2020

@author: joanluc

--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way 
down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. 
"Something's wrong with our computers; we can't log in!" You ask if you can 
take a look.

Their password database seems to be a little corrupted: some of the passwords 
wouldn't have been allowed by the Official Toboggan Corporate Policy that was 
in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of 
passwords (according to the corrupted database) and the corporate policy when 
that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy 
indicates the lowest and highest number of times a given letter must appear 
for the password to be valid. For example, 1-3 a means that the password must 
contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is 
not; it contains no instances of b, but needs at least 1. The first and third 
passwords are valid: they contain one a or nine c, both within the limits of 
their respective policies.

How many passwords are valid according to their policies?

To begin, get your puzzle input.

Answer:
You can also [Shareon Twitter Mastodon] this puzzle.
"""
def parsePolicy(policy):
    polNbs=policy.split(" ")[0]
    polCar=policy.split(" ")[1]
    polNb1=polNbs.split("-")[0]
    polNb2=polNbs.split("-")[1]
    return(polNb1,polNb2,polCar)

def passwordVerif(policy,passwd):
    polNb1=parsePolicy(policy)[0]
    polNb2=parsePolicy(policy)[1]
    polCar=parsePolicy(policy)[2]
    import regex as re
    reg=re.search(polCar+"{"+polNb1+","+polNb2+"}",passwd)
    if reg!=None:
        return(True)
    else:
        return(False)

    
def listFile(finame):
    l=list()
    f=open(finame,"r")
    for n in f:
        l.append(n)
    f.close()
    return(l)

nPassOk=0
l=listFile("input2")   
for line in l:  
    policy=line.split(":")[0]
    passwd=line.split(":")[1]
    if passwordVerif(policy,passwd)==True:
        nPassOk=nPassOk+1
print(format(nPassOk))
    

