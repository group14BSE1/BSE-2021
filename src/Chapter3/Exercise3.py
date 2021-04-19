# Prompt for score from the user between 0.0 to 1.o
score_raw = input("Enter a score:")

# check if score is numeric and within the range
try:
    score = float(score_raw)
    if 0 < score < 1.0
        if score >= 0.9:
            print(score, "A")
        elif score >= 0.8:
            print(score, "B")
        elif score >= 0.7:
            print(score, "C")
        elif score >= 0.6:
            print(score, "D")
        elif score < 0.6:
            print(score, "F")
    else:
        print("Error, the entered value is out of range")
except:
    print("Error, enter numeric input")