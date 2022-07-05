# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:56:11 2022

@author: Harish
"""

all=[]
n = int(input())
for i in range(n):
    all.append(i+1)
str1=""
for a in all:
    str1 += str(a)
print(str1)