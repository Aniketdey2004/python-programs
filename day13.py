#strings are immutable, when method changes a particular string it makes changes on the copy of the string
a="Harry"
print(a.lower())#converts entire string to lowerCase
print(a.upper())#converts entire string to Uppercase
string="Aniket!!! Aniket!!! Aniket!!!"
print(string.rstrip("!")) #removes the trailing characters
print(string.replace("Aniket","Soumashree")) #replaces every occurence of a particular string with a new string
print(string.split(" ")) #splits the string into list elements based on separator in brackets
sen="sPooN"
print(sen.capitalize())#makes the first character of string uppercase and the rest to lowercase
str1="Welcome to the console!!!"
print(str1.center(50)) #it centres the string in the output window based on parameter
print(string.count("Aniket"))#counts the number of occurence of a particular string

print(string.endswith("!!!")) #return bool value on whether a string ends with a particular string
print(string.endswith("!!!",0,9)) #does similar work but sees range

print(string.startswith("Aniket"))#return true if string starts with a particular string

print(string.find("!")) #gives the index of first occurence of a string if string not found returns -1 
print(string.index("!")) #does similar work as find() function but throws error if string not found

print(a.isalnum()) #return true if a string contains A-Z,a-z,0-9
print(a.isalpha()) #return true if a string contains A-Z,a-z

print(a.islower()) #return true if all characters in a string are lowercase
print(a.isprintable())#return true if all the characters of the string can be printed on terminal

g="hi,\n i am aniket"
print(g.isprintable()) #return false because escape charcters that cannot be printed ere present

h="      "
print(h.isspace()) #return true if the string contains only blank spaces

f="This Is A Sentence"
print(f.istitle()) #checks whether first character of every word is capital or not

print(f.swapcase())#converts uppercase to lowercase and lowercase to uppercase


print(str1.title()) #converts the given string into title case

