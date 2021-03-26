# ask user to enter their temperature in celsius
celsius_temp = float(input("Please enter temperature(Celsius) to convert to Fahrenheit"))

# formula : Fahrenheit = C * (9/5) + 32
fah_temp = (celsius_temp * (9/5)) + 32

print("The entered temperature in Celsius is: ", fah_temp, "Degrees Fahrenheit")
