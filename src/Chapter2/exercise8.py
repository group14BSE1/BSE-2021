# enter initial amount of investment
c_init = int(input("Enter initial amount of investment:"))
r_rate = float(input("Enter the yearly rate of interest:"))
t_yrs = int(input("Enter number of years till maturation:"))
n_times = int(input("Enter number of times the interest is compounded:"))
# =====================================================================================
# Formula to be implemented
# p = c(1 + r/n)^tn round to 2dp
# =====================================================================================
# addition done after division
add_part = 1 + (r_rate/n_times)

# The expression is then raised to [tn] - (t_yrs*n_times)
final_expr = add_part ** (t_yrs*n_times)

# result is multiplied with the initial value
final_value = c_init * final_expr

# Final value rounded using the round function to 2 dp
rounded_value = round(final_value, 2)

# Rounded final value of investment is printed
print(rounded_value)
