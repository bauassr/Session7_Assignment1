# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 12:49:09 2018

@author: singh.shivam
"""
import numpy as np

In_lst =[3,5,7,2,8,10,11,65,72,81,99,100,150]
k=3

def RAvg(lst,k):
    print(lst)
    print("=============Using Numpy array ================")
    n=len(lst)-k+1
    
    for i in range(n):
        temp=0
        strn=""
        for j in lst[i:i+3]:
            if len(strn) > 0 :
                strn= strn +"+"+str(j)
            else:
                strn="( "+str(j)
            temp+=j
        print("y"+str(i+1),end="")
        for a in range((i+1)*4):
             print(" ",end="")
        print(temp/k,"=",strn,")")
         
def Run_avg(Lst,k):
    print(Lst)
    print("++++++++++++Using standard Python++++++++++++++++")
    n=len(Lst)-k+1
    Lst = np.array(Lst)
    for i in range(n):
        strn=""
        #numpy Split 
        Lst_j = np.split(Lst,[i,i+k])
        for j in Lst_j[1]:
            if len(strn) > 0 :
                strn= strn +"+"+str(j)
            else:
                strn="( "+str(j)
        print("y"+str(i+1),end="")
        for a in range((i+1)*4):
             print(" ",end="")
        #numpy Sum 
        print(np.sum(Lst_j[1])/3,"=",strn,")")    
       
        
        
Run_avg(In_lst,k)
RAvg(In_lst,k)