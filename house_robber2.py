'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''

def rob(nums):
    
    if not len(nums):
        return 0
    
    # If array has no more than three elements,
    # as it is a circular array we can only select
    # one of the three elements.
    if len(nums) <= 3:
        return max(nums)
    
    n = len(nums)
    
    # Function to solve the subproblem
    def maxAmountRobbed(nums):
        if not len(nums):
            return 0
        
        if len(nums) <=2:
            return max(nums)
        m = len(nums)
        t = dict()
        
        t[0] = nums[0]
        # When first two elements are scanned
        t[1] = max(nums[0], nums[1])
        
        # Scanning from second elements onwards
        for i in range(2, m):
            t[i] = max(nums[i]+t[i-2], t[i-1])
            
        return t[m-1]
    
    # IF we take 0th value we have to consider next possible
    # values are upto n-1, as 0 and n are connected
    res1 = maxAmountRobbed(nums[0:n-1])
    
    # IF we take 1th value we have to consider next possible
    # values up to n, as 0 and n are connected
    res2 = maxAmountRobbed(nums[1:n])
    return max(res1, res2)

nums1 = [2,3,2]
nums2 = [1,2,3,1]
nums3 = [1,2,3]

print(rob(nums1))
print(rob(nums2))
print(rob(nums3))
