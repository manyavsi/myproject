def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string
 
print(is_palindrome('mom')) # True
print(is_palindrome('whatisit')) # False