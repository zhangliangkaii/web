# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:08:15 2018

@author: zhangliangkai
"""

import random

n = random.randint(3, 10)

l = [0] * n
for i in range(n):
    l[i] = random.randint(1, 10)
total = sum(l)

table = [0] * n
for i in range(n):
    table[i] = [0] * (total+1)

whether = [0] * n
for i in range(n):
    whether[i] = [0] * (total+1)

for i in range(n):
    for j in range(total+1):
        if l[i] < j:
            if(abs(table[i-1][j]-total//2) <
               abs(table[i-1][j-l[i]]+l[i]-total//2)):
                table[i][j] = table[i-1][j]
                whether[i][j] = 0
            else:
                table[i][j] = table[i-1][j-l[i]] + l[i]
                whether[i][j] = 1
        print(table[i][j], end=' ')
    print('')

x = []
y = []
row = n-1
col = total//2 + 1
while(row >= 0):
    if(whether[row][col]):
        x.append(l[row])
        col = col - l[row]
        row = row - 1
    else:
        y.append(l[row])
        row = row - 1

print('group1:', end='')
print(x)
print('group2:', end='')
print(y)
print('weight:', end='')
print(sum(x), sum(y))
