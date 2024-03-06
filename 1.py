# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:56:46 2024

@author: 孟刚
"""
ans=0
for x in range(3,1001,2):
    for y in range(2,x):
        if x%y==0:
            break
    else: ans+=x
print(ans+2)

print('第一次修改')