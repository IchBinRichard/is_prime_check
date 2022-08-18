#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:04:30 2022

@author: lijiaheng
"""

# 1~100質數判斷
# 大於1，且無法找到除了自己本身和1之外的自然數能整除它的自然數
# ex: 2, 3, 5, 7, 11, 13

def printPrime (num): #判斷1到某數之間有幾個質數
    count = 0
    if num == 0:
        print('0不是質數')
    for i in range(1,num+1):
        if(is_prime(i) == '是'):
            count += 1
            print(i,end = (' '))
    print('\n1 到 %3d 有 %2d 個質數' %(num,count))
        
number = int(input('判斷1到某數之間有幾個質數：'))                    
printPrime(number)





    

