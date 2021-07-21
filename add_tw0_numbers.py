'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Approach
'''
Intuition

Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.


Algorithm

Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of l1l1 and l2l2. Since each digit is in the range of 0 \ldots 90…9, summing two digits may "overflow". For example 5 + 7 = 125+7=12. In this case, we set the current digit to 22 and bring over the carry = 1carry=1 to the next iteration. carrycarry must be either 00 or 11 because the largest possible sum of two digits (including the carry) is 9 + 9 + 1 = 199+9+1=19.

***The pseudocode is as following:

Initialize current node to dummy head of the returning list.
Initialize carry to 00.
Initialize pp and qq to head of l1l1 and l2l2 respectively.
Loop through lists l1l1 and l2l2 until you reach both ends.
Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
Set sum = x + y + carrysum=x+y+carry.
Update carry = sum / 10carry=sum/10.
Create a new node with the digit value of (sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
Advance both pp and qq.
Check if carry = 1carry=1, if so append a new node with digit 11 to the returning list.
Return dummy head's next node.


Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.

Take extra caution of the following cases:

Test case	Explanation
l1=[0,1]
l2=[0,1,2]	When one list is longer than the other.

l1=[]
l2=[0,1]	When one list is null, which means an empty list.

l1=[9,9]
l2=[1]	The sum could have an extra carry of one at the end, which is easy to forget.
'''

# Definition for singly-linked list.
class ListNode: #creates nodes with default values as 0 and None
    def __init__(self, val=0, next=None): 
        self.val = val
        self.next = next

class Solution: #need to return a ListNode
    def add_two_nums(self, l1, l2):
        dummy = ListNode() #head of returning list
        cur = dummy #pointer to dummy ListNode
        carry = 0
        
        while l1 or l2 or carry: #Thus will loop until l1 == None  and l2 == None and carry == 0
            v1 = l1.val if l1 else 0 # v1 = value of l1 if it is not None else l1.val = 0
            v2 = l2.val if l2 else 0 
            
            val = v1 + v2 + carry #sum
            carry = val // 10 
            val = val % 10 # the ones place of val
            
            cur.next = ListNode(val)
            #created a ListNode with val(not zero) and we assigned to cur.next, so the cur.next will now have the address of new ListNode
            
            cur = cur.next #moving our current pointer to next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next  # we will not return dummy as it also contain a default value 0

'''Complexity Analysis
Time Complexity: O(max(m, n)) where m, n are lengths of l1, l2 respectively since the algorithm above iterates at most max(m, n)
times

Space Complexity: O(max(m,n)). The length of the new list will be max(m, n)+ 1
'''
