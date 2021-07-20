'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.


Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
'''

import math
def getSum(a,b):
    return int(math.log2(pow(2, a) * pow(2, b))) #math returns a float point we need to type cast it to int
print(getSum(12,3))


# This method is faster than the previous one 
def getSum2(a,b):
    if b > 0:
        while(b>0):
            a += 1
            b -= 1
    elif b < 0:
        while(b < 0):
            a -= 1
            b += 1
    return a

print(getSum2(12, 14))
            