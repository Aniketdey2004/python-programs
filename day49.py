f=open("Aniket.txt",'r')
text=f.read()
print(text)
f.close()

with open("Aniket.txt",'w') as f:
    f.write("i also write very good programs")

f=open("Aniket.txt","w")
f.write("they are new text")
f.close()

with open("Aniket.txt",'a') as f:
    f.write("i also write very good programs")
f=open("Aniket.txt",'a')
f.write("i am mern stack developer")
f.close()

with open("Aniket.txt",'r') as f:
    text=f.read()
    print(text)
