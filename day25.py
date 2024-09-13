#tuples are immutable they can only be changed by first converting them into list then modify and again convert them to tuple
countries=("Bangladeesh","India","Malaysia","usa")
print(countries.count("Bangladesh"))#counts the no. of items element is present
print(countries.index("India"))#return the first index of element