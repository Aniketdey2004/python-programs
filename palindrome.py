s=input("enter a string: ")
def isPalindrome(s):
    h=""
    for i in range(len(s)-1,-1,-1):
        h=h+s[i]
    if(h==s):
        return True
    else:
        return False

check=isPalindrome(s)
if(check==True):
    print("palindrome")
else:
    print("not a palindrome")