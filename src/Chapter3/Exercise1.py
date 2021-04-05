# Ask for the number of hours worked
hours_wkd = int(input("Enter the number of hours worked:"))

# Enter the hourly rate
rate_hr = float(input("Enter the Rate:"))

# for hours above 40 ; the rate entered is multiplied by 1.5
# The product of that multiplication is used to calculate the gross pay
if hours_wkd > 40:
    rate_new = 1.5 * rate_hr
    gross_pay = hours_wkd * rate_new
    print("Pay:", gross_pay)
else:
    # If the hours are below or equal to 40 the entered rate is then used to calculate the Gross pay
    gross_pay = hours_wkd * rate_hr
    print("Pay:", gross_pay)