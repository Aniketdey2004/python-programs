def isEligible(age):
    if age >= 18:
        print("The person can vote")
    else:
        print("The person cannot vote")

while True:
    x = input("Enter age to check eligibility and 'done' or 'exit' to quit: ")
    if x.lower() in ['done', 'exit']:
        break
    elif x.isdigit():
        isEligible(int(x))
    else:
        print("Please enter a valid number or 'done'/'exit' to quit.")
