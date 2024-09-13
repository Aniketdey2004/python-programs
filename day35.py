for i in range(6):
    print(i)
else:#the else is executed after all the iteration of loop is completed and the loop has successfully ended
    print("the loop has ended")

i=0
while i<7:
    print(i)
    i=i+1
else:
    print("the while loop is finished")

while i<7:
    print(i)
    i=i+1
    if(i==4):
        break #the loop has not ended and breaked so the else part will not be executed
else:
    print("the while loop is finished")