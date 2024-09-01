import time
timestamp=int(time.strftime('%H'))

if(timestamp>=4 and timestamp<12):
    print("Good morning soumashree")
elif(timestamp>=12 and timestamp<18):
    print("Good afternoon soumashree")
elif(timestamp>=18 and timestamp<22):
    print("Good evening soumashree")
else:
    print("Good night soumashree")