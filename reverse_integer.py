'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1'''

# Method 1
def reverse_int(x):
    if x >= 0:
        ans = int(str(x)[::-1])
    else:
        ans = -int(str(-x)[::-1]) #making integer positive, converting into string , reversing the string, converting back into integer and adding minus to it
    
    if ans >= -2 ** 31 and  ans <= 2**31 -1:
        return ans
    return 0


# Method 2
def reversed_int(x):
    def validate_32bit(reversed_int):
        if reversed_int in range(-2**31, 2**31-1): #checking if the number is in the range or not
            return reversed_int
        else:
            return 0
                
    try: 
        reversed_int = int(str(x)[::-1]) #converting into string, reversing the string and then converting again into int, ifgiven is negative number "int" will throw ValueError
        return validate_32bit(reversed_int)
    except ValueError:
        str_x = str(x)
        if str_x.startswith('-'):
            return validate_32bit(-1*int(str_x.replace('-', '')[::-1])) #replacing the '-' with no character and then reversing the string
        
print(reversed_int(-123))


# Cpp code --> Faster than python codes

# class Solution{
#   public:
#       int func(int n, int rev){
#         if (n==0) # base case
#             return rev;
#         if (rev > INT32_MAX/10 || rev < INT32_MIN/10) #checking 
#             return 0;
#         rev = 10 * rev + (n % 10); #updated rev
#         return func(n/10, rev);
#       }
#       int reverse(x){
#           return func(x, 0) #recursive call
#       }  
# };