'''
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.


Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''

class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def twoSum(self):
        l, r = 0, len(self.nums)-1 #left and right pointers indicating the start and end positions of the list
        while l < r:
            curSum = self.nums[l] + self.nums[r]
            if curSum < self.target:
                l += 1 #left pointer moves ahead of an index of 1
            elif curSum > self.target:
                r -= 1 #right pointer moves behind of an index of 1
            else:
                return [l+1, r+1]
        return [] #if solution exists

List = [2,7,11,15]
target =  9  
sol = Solution(List, target)
print(sol.twoSum())
# Time complexity: O(n)