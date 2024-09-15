f=open("myfile.txt",'r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()
f=open("myfile.txt",'w')
lines=['line1','line2']
f.writelines(lines)
f.close()