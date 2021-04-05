# prompt for the number of guests
guest_number = input("Enter the number of expected guests:")

# Check if input is numeric
try:
    guest_exact = int(guest_number)
    if guest_exact <= 50:
        print("It will cost $4000 dollars!")
    else:
        if guest_exact <= 100:
            print("It will cost $10000 dollars!")
        else:
            if guest_exact <= 200:
                print("It will cost $15000 dollars!")
            else:
                if guest_exact > 200:
                    print("It will cost $20000 dollars!")


# Throw an error if input is not numeric
except:
    print("Error , Please enter numeric input!")
