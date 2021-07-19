'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort() #sorts the list in ascending order #O(nlog(n))
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # we dont want to consider same 'a'
                continue
            l, r = i + 1, len(nums) - 1 #left pointer after 'a' and right pointer end of the list
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) #sol gets added here 
                    l += 1 #then we need to update the pointer and also we dont the pointer just as before because we dont the duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res # Fianl result 

List = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(List))

# Time Complexity: O(nlog(n)) + O(n^2) --> O(n^2)
# Space Complexity: O(1) or O(n) depends on the implementation of sorting