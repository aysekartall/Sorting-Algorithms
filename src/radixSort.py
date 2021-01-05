# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 20:58:50 2021

@author: AYSE
"""
import time 

def counting_sort(array, exp):
    n = len(array)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        index = array[i] / exp
        count[int(index % 10)] += 1
    for i in range (1, 10):
        count[i] += count[i-1]
    i = n-1
    while i >=0:
        index = array[i] / exp
        output[count[int(index % 10)] - 1] = array[i] 
        count[int(index % 10)] -= 1
        i -= 1
  
    for i in range(0, n): 
        array[i] = output[i] 
  
def radixSort(array): 
  
    max_num = max(array) 
    exp = 1
    for i in range(len(str(max_num))):
        counting_sort(array, exp) 
        exp *= 10


numbers = open("sortdata.txt").read().split()
numbers = [int(number) for number in numbers]

start_time = time.time()           

print (("sırasız dizi: "), numbers)
radixSort(numbers)
stop_time = time.time() 
print (("sıralı dizi: "), numbers)
print("geçen zaman", stop_time - start_time)   