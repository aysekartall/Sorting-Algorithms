# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:42:45 2021

@author: AYSE
"""
import time

def insertion_sort(dizi):
    for i in range(1, len(dizi)):
        key = dizi[i]
        j = i - 1
        
        
        while j >= 0 and key < dizi[j]:
            dizi[j+1] = dizi[j]
            j = j - 1
        dizi[j + 1] = key
         
 
numbers = open("sortdata.txt").read().split()
numbers = [int(number) for number in numbers]

start_time = time.time()           

print (("sırasız dizi: "), numbers)
insertion_sort(numbers)
stop_time = time.time() 
print (("sıralı dizi: "), numbers)
print("geçen zaman", stop_time - start_time)