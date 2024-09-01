s=input("enter a sentence: ")
def reverse(s):
    h=""
    for i in range(len(s)-1,-1,-1):
        h=h+s[i]
    return h

rev=reverse(s)
print("reverse=",rev)