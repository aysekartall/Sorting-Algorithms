# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:17:27 2021

@author: AYSE
"""
import time

def merge(dizi):
   # print ("parçalanan değerler " + str(dizi))
    if len(dizi) > 1:
        orta = len(dizi) // 2
        solDizi = dizi[:orta]
        sagDizi = dizi[orta:]
        
        merge(solDizi)
        merge(sagDizi)
        mergeSort(dizi, solDizi, sagDizi)
        
def mergeSort(dizi, solDizi, sagDizi):
    i = 0
    j = 0
    k = 0
    
    while i < len(solDizi) and j < len(sagDizi):
        
        if solDizi[i] < sagDizi[j]:
            dizi[k] = solDizi[i]
            i = i + 1
        else:
            dizi[k] = sagDizi[j]
            j = j + 1
        k = k + 1
    
    while i < len(solDizi):
        dizi[k] = solDizi[i]
        i = i + 1
        k = k + 1
        
    while j < len(sagDizi):
        dizi[k] = sagDizi[j]
        j = j + 1
        k = k + 1
   # print ("Birleştirilmiş hali " + str(dizi))
  
   
numbers = open("sortdata.txt").read().split()
numbers = [int(number) for number in numbers]

start_time = time.time()           

print (("sırasız dizi: "), numbers)
merge(numbers)
stop_time = time.time() 
print (("sıralı dizi: "), numbers)
print("geçen zaman", stop_time - start_time)
        
            