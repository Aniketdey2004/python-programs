#dictionary is a combination of key value pairs
dic={
    "Harry":"human being",
    "Tamojit":"januar",
    "Aniket":"boro januar",
    "Soumashree":"ultra pro max januar"
}
print(dic["Soumashree"]) #access elements by their key
print(dic.get("Tamojit"))#access element other way
#by both ways value can be accesssed but first method raises error if key not found and get() return None

print(dic.keys())#we can see all the keys of a dictionary
print(dic.values())#we can see all the values
print(dic.items())#if we want to see all the key value pairs

#we can print all the keys along with their values
for key in dic:
    print(f"the value of the key {key} is {dic.get(key)}")


for key,values in dic.items():
    print(f"the value corresponding to the key {key} is {values}")