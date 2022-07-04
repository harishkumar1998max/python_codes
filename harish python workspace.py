# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 12:58:15 2022

@author: Harish
"""
#swapping list
#Python program to interchange first and last elements in a list 
#Given a list, write a Python program to swap first and last element of the list.
#Input : [1, 2, 3]
#Output : [3, 2, 1]#

def swaplis(swap,pos1,pos2):
    swap[pos1],swap[pos2]=swap[pos2],swap[pos1]
    return swap
list=[12,35,9,56,24]
pos1,pos2=1,5
print(list)
print("swapped list:",swaplis(list,pos1-1,pos2-1))


#find smallest number in a list
#Python program to find smallest number in a list
#Given a list of numbers, the task is to write a Python program to find the smallest number in given list.
#Input : list1 = [10, 20, 4]
#Output : 4

list1=[23,56,84,95,22,16,44]
print('smallest number in ths list:',min(list1))
    
