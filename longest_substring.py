'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

# Sliding technique

def longestSubstring(s):
    longest = 0 #keep track of longest substring
    charSet = set() #empty set
    lp = 0 #left pointer and rp is rigth pointer 
    for rp in range(len(s)): #from 0 to len(s) -1
        while s[rp] in charSet: # while the character pointed by right pointer in charSet, start removing the character pointed by left pointer until the character we wanted was removed
            charSet.remove(s[lp])
            lp += 1 #after removing the character pointed by left pointer, we need to move left pointer to next one
        charSet.add(s[rp]) #if the character not present in set, then add it to the list. (Even if the duplicate will be added here once we remove the original character which is already present in the list)
        
        longest = max(longest, rp - lp + 1) #keep updating the longest variable by checking using max method
    return longest # Once we done with the string, we will the value of longest

print(longestSubstring("abcabcbb"))
print(longestSubstring("bbbb"))
print(longestSubstring("pwwkew"))
print(longestSubstring("123 456"))

'''
Time Complexity: O(n) as we are iterating the string only once.
Space Complexity: O(n) if all the characters string are unique
'''