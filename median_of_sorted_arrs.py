'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

def median(nums1, nums2):
    nums = [*nums1, *nums2] # deferencing the lists.. if nums1 = [1,3] and [2,3] then nums = [1,3,2,3]
    nums.sort() # O((n+m)log(n+m))
    l = len(nums) #length of merged array
    if l%2==0: #even
        return (nums[int(l/2)] + nums[int(l/2 - 1)])/2 #middle term and left neighborhood of middle term;
        #returns median value (float data type)
    else:
        return nums[l//2] #floor division we get a valid index 
    
'''
Time complexity: O((n+m)log(n+m)) for sorting of merged array
Space Complexity: O(n+m) for merged array
'''

def median2(nums1, nums2):
    A, B = nums1, nums2 
    total = len(nums1) + len(nums2) #total number of elements
    half = total // 2 #half of the total in int data type
    # assuming A has least number of elements because we need to use binary search for one of them
    if len(B) < len(A): #if length of A is more than length of B, then we need to swap them
        A, B = B, A #swaping arrays
    # Now , A will be the smallest array
    l , r = 0, len(A)-1 #points to index 0 and last element of the list A
    while True:
        i = (l+r) // 2 # A midpoint index (A's left part)
        j = half - i - 2 # B (B's left part) , j = index
        
        Aleft = A[i] if i>=0 else float("-infinity") # if A is an empty list then A[i] will be -infinity
        Aright = A[i+1] if i+1 < len(A) else float("infinity")
        # if we use all the elements of A for left partition then we will be no more elements left to use.Hence we use A[i+1] as "infinity"
        Bleft = B[j] if j>=0 else float("-infinity") #similarly for the B list
        Bright = B[j+1] if j+1 < len(B) else float("infinity")
        
        if Aleft <= Bright and Bleft <= Aright: #This checks that the left partition which we did correct or not
            if total % 2: #Odd number of elements
                return min(Aright, Bright) #minumun of the two will be the median for the list
            return (max(Aleft, Bleft) + min(Aright, Bright))/2 #since we need to find the median for the sorted array
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1 #left pointer moves to middle term + 1 and then repeats the process . What it does is it increases the left partiton size of A and decreases the left partition of B
        
'''
Time Complexity: O(log(min(n,m))) since we are only doing binary search for the smaller array
'''           
     

print(median([1,3],[2]))
print(median([1,2],[3,4]))

print(median2([1,3],[2]))
print(median2([1,2],[3,4]))
