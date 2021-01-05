# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:54:06 2021

@author: AYSE
"""
import time

def bubble_sort(dizi):
    for i in range(len(dizi) - 1):
        for j in range(len(dizi) -1 - i):
            if dizi[j] > dizi[j + 1]:
                dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j]
       
  
numbers = open("sortdata.txt").read().split()
numbers = [int(number) for number in numbers]

start_time = time.time()           

print (("sırasız dizi: "), numbers)
bubble_sort(numbers)
stop_time = time.time() 
print (("sıralı dizi: "), numbers)
print("geçen zaman", stop_time - start_time)        

