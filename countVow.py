s=input("enter a string: ")
def countVowel(s):
    c=0
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            c=c+1
    return c

c=countVowel(s.lower())
print("no. of vowels=",c)