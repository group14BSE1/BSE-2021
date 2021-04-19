# Prompt for score from the user between 0.0 to 1.o
score_raw = input("Enter a score:")

# check if score is numeric and within the range
def compute_grade(score_feed):
    try:
        # check if the required input was the one provideds
        score = float(score_feed)
        grade = ""
        if 0 < score < 1.0:
            if score >= 0.9:
                grade = "A"
            elif score >= 0.8:
                grade = "B"
            elif score >= 0.7:
                grade = "C"
            elif score >= 0.6:
                grade = "D"
            elif score < 0.6:
                grade = "F"
        else:
            print("Error, the entered value is out of range")

        # return the grade using the return statement
        return grade
    except:
        print("Error, enter numeric input")

# check if the user entered something
if len(score_raw) > 0:
    result = compute_grade(score_raw)

    print(score_raw, ":", result)
else:
    print("Error, please enter something!")
