
#! M-1
def is_palindrome1(n):
    rev=n[::-1]
    if n==rev:return True
    else:return False

#! M-2  
def is_palindrome2(n):
    if n==n[::-1]: return True
    return False

#! M-3  ----------> Best
def is_palindrome3(n):
    return n==n[::-1]

n=str(input())
print(is_palindrome1(n))
print(is_palindrome2(n))
print(is_palindrome3(n))



