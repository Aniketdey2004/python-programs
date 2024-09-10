x = int(input("Enter your choice: "))

match x:
    case 1:
        print("You chose option 1")
    case 2:
        print("You chose option 2")
    case 3:
        print("You chose option 3")
    case _ if x>30:
        print("x grater than 30")
    case _:
        print("Invalid choice") #there can be more than one default cases
    