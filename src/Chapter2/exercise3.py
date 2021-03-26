# Program to prompt the user for hours and rate per hour and it computes the gross pay

# prompted user for the hours
hours_entered = input("Enter hours:")

# Prompted the user for the rate
rate_entered = input("Enter the rate:")

# Converted the entered strings to int and float respectively
# after multiplied them and stored the result in pay_generated
pay_generated = int(hours_entered) * float(rate_entered)

# Rounded off result to 2dp using the built in round function
rounded_pay = round(pay_generated, 2)

print("Gross Pay:", rounded_pay)