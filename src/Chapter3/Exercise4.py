# prompt for age input
user_age = input("Please Enter your age:")

# Check if input is numeric
try:
    verified_age = int(user_age)
    if verified_age >= 18:
        print("You can vote")
    elif 0 < verified_age <= 17:
        print("Too young to vote")
    elif verified_age < 0:
        print("Your a time traveler")

# Throw an error if input is not numeric
except:
    print("Error , Please enter numeric input!")
