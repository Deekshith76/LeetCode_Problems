'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self): #Brute method #yime compelxity: O(n^2)
        length = len(self.nums)
        for i in range(length):
            for j in range(i+1, length):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i,j]
        return []
    
    def twoSumOpt(self): #Optimal Solution ; Time Complexity: O(n) for iterating through the array once; Space Complexity: O(n) for hashmap
        prevMap = {} # value: index
        for i, n in enumerate(self.nums):
            # print(i, n)
            diff = target - n
            if diff in prevMap:
                # print(prevMap)
                return [prevMap[diff], i]
            prevMap[n] = i
        return []

List = [4,2,11,7,8,-1,9,18,10]
target = 21
sol = Solution(List, target)
print(sol.twoSum())
print(sol.twoSumOpt())                 
            