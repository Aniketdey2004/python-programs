def welcome():
    print("good morning")
#welcome() 
"""like this when it is imported everything in this program will be executed to avoid this we will use __name__ which is set to __main__ in current file and when imported it is set to file name"""
if __name__=="__main__": #we want to execute the statements if the original file  is run not when imported
    welcome()

