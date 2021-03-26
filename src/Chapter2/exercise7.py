# accept a given amount of money in dollars and the result is change
# Available currency notes
# twenty_dollar, ten_dollar, five_dollar, one_dollar = 20, 10, 5, 1

# Available currency coins
# quarter_25cents, dime_10cents, nickel_5cents, penny_1cent = 25, 10, 5, 1
entered_currency = float(input("Enter amount to make change:"))
# get no of twenty dollars
twenty = entered_currency // 20
# remainder after getting 20 dollars
remainder_twenty = entered_currency % 20

# used remainder of twenty  to find 10 dollars
ten = remainder_twenty // 10
# remainder after getting tens
remainder_ten = remainder_twenty % 10

# used remainder of ten to find 5 dollars
fives = remainder_ten // 5
# remainder after getting fives
remainder_five = remainder_ten % 5

# get 1 dollars using remainder of 5 dollars
ones = remainder_five // 1
remainder_one = remainder_five % 1

# get quarter cents using remainder of 1 dollars
quarters = remainder_one // 0.25
remainder_quarter = remainder_one % 0.25

# get dime cents using remainder of quarter cents
dimes = remainder_quarter // 0.1
remainder_dime = remainder_quarter % 0.1

# get nickel cents using remainder of dime cents
nickles = remainder_dime // 0.05
remainder_nickle = remainder_dime % 0.05

# get penny cents using remainder of nickle cents
penny = remainder_nickle // 0.01


print("Your change is ......")
print(round(twenty), "Twenties")
print(round(ten), "Tens")
print(round(fives), "Fives")
print(round(ones), "Ones")
print(round(quarters), "Quarters")
print(round(dimes), "Dimes")
print(round(nickles), "Nickles")
print(round(penny), "Pennys")