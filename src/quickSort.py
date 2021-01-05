# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:49:21 2021

@author: AYSE
"""
import time

def parcala(dizi, solIndis, sagIndis):
    i = solIndis - 1
    pivot = dizi[sagIndis]
    
    for j in range(solIndis,sagIndis):
        if dizi[j] <= pivot:
            i = i +1
            dizi[i],dizi[j] = dizi[j],dizi[i]
    dizi[i+1],dizi[sagIndis] = dizi[sagIndis],dizi[i+1]
    return i + 1
    
def quicksort(dizi, solIndis, sagIndis):
    if solIndis < sagIndis:
        pivot = parcala(dizi, solIndis, sagIndis)
        quicksort(dizi, solIndis, pivot - 1)
        quicksort(dizi, pivot + 1, sagIndis)
        
        
numbers = open("sortdata.txt").read().split()
numbers = [int(number) for number in numbers]

start_time = time.time()           

print (("sırasız dizi: "), numbers)
quicksort(numbers, 0, len(numbers) - 1)
stop_time = time.time() 
print (("sıralı dizi: "), numbers)
print("geçen zaman", stop_time - start_time)

