def palindrome(x):
    string = str(x) #converting integer to string
    revString = string[::-1] #reversing the string and storing it in the revString
    if string == revString: #checking
        return True
    else:
        return False
    # one liner for above code --> return str(x) == str(x)[::-1]

# This method do not involve conversion to a string , hence it is much faster
def palindrome2(x):
    if x < 0: # for negaitve numbers
        return False
    rev, temp = 0, x
    while temp:
        rev = 10 * rev + (temp%10) #keeps updating the rev variable
        temp //= 10 # Dont forget to floor divide this thing
    return x == rev 

print(palindrome(121))
print(palindrome2(121))
        
    


