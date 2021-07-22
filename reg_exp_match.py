'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''
# Recursive Solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # TOP- Down memoization 
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j+1] == '*':
                return dfs(i, j+2) or (match and dfs(i+1, j))
            if match:
                return dfs(i+1, j+1)
            return False
        return dfs(0,0)

# memoized solution   
class Solution2:
    def isMatch(self, s: str, p: str, cache = None) -> bool:
        # TOP- Down memoization
        if cache is None:
            cache = {} # keeps track of sub problems which we solved in the process
        def dfs(i, j): #checks if i, j pointers or not
            if (i, j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p): # if both pointers came to end at the same point then the desirable is achieved, hence we will return True
                return True
            if j >= len(p): #if pattern pointer is out of bound before string pointer then False ( no way we can make the remaining string)
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".") # checks if i is in range and also checks the element pointed by i, j are same or not. Also it checks if j pointer to (".") symbol
            if (j + 1) < len(p) and p[j+1] == '*': #if j's next character is "*" and j+1 is also in the range then True
                cache[(i,j)] =  dfs(i, j+2) or (match and dfs(i+1, j))
                # we have 2 choices when we get "*" , either we can use "" or we can the repeat the preceeding character.
                #if we are choosing the "", then j pointer moves 2 steps ahead so that we can go beyond the "*"
                # but if the repeating the character then i pointer for the string moves ahead by 1
                return cache[(i,j)]
            if match:
                # if we are checking only for the alphabets and if they match, then we move both pointers to 1 step ahead
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return cache[(i,j)]
        
        return dfs(0,0) 
    
sol = Solution2()
sol = Solution2()
print(sol.isMatch("mississippi", "mis*is*p*."))
print(sol.isMatch("aa","a*"))