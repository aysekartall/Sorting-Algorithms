# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 21:24:08 2021

@author: AYSE
"""
import time

def max_heap(arr,n,parent_idx):
    largest = parent_idx
    left = 2*parent_idx + 1
    right = 2*parent_idx + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != parent_idx:
        arr[largest], arr[parent_idx] = arr[parent_idx], arr[largest]
        max_heap(arr, n, largest)
        
def heapsort(arr):
    n = len(arr)
    
    for i in range(n // 2 -1,-1,-1):
        max_heap(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heap(arr, i, 0)
        

numbers = open("sortdata.txt").read().split()
numbers = [int(number) for number in numbers]

start_time = time.time()           

print (("sırasız dizi: "), numbers)
heapsort(numbers)
stop_time = time.time() 
print (("sıralı dizi: "), numbers)
print("geçen zaman", stop_time - start_time) 