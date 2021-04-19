def pay_determiner(c,r,n, t):
    # formula to follow
    # p = c(1+ (r/n)) ** tn
    start = 1 + (r/n)
    end = start ** t*n
    final = start * end
    return  round(final, 2)

initial = 1000
rate = 0.01
num = 1
time = 1

final_value = pay_determiner(initial, rate, num, time)
print("Final value:", final_value)