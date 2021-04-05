# Ask for the number of hours worked
hours_wkd = input("Enter the number of hours worked:")

# Enter the hourly rate
rate_hr = input("Enter the Rate:")

# check if the hours worked and rate are numeric
try:
    # The input is tried to be converted to the float data type
    exact_hrs = float(hours_wkd)
    exact_rate = float(rate_hr)

    # If the input is numeric , it means it can be converted
    # Hence the gross pay is calculated
    gross_pay = exact_hrs * exact_rate
    print("Pay:", gross_pay)

except:
    # If the conversion to numeric data types fails an error is thrown
    print("Error, please enter numeric input")

