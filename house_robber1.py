'''
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''

def rob(nums): #int -> money stolen
    rob1 , rob2 = 0, 0
    
    # [rob1, rob2, n, n+1, n+2, ...]
    for n in nums:
        current  = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = current
    
    return rob2

nums1 = [2,7,9,3,1]
nums2 = [1,2,3,1]
print(rob(nums1))
print(rob(nums2))

    
