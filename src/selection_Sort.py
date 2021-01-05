# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:47:53 2021

@author: AYSE
"""
import time

def selection_sort(dizi):
    for i in range(len(dizi)):
        min_index  = i
        for j in range(i + 1, len(dizi)):
            if dizi[min_index] > dizi[j]:
                min_index = j
        if min_index != i:
            dizi[min_index], dizi[i] = dizi[i], dizi[min_index]
            
                 
numbers = open("sortdata.txt").read().split()
numbers = [int(number) for number in numbers]

start_time = time.time()           

print (("sırasız dizi: "), numbers)
selection_sort(numbers)
stop_time = time.time() 
print (("sıralı dizi: "), numbers)
print("geçen zaman", stop_time - start_time)