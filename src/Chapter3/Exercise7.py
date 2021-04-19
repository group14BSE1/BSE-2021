# prompt for the area or location of the work
job_area = input("Enter the Location of work:")

# prompt for the wage of the job
job_wage = input("Enter The wage provided:")

# Check if the user entered something at both data entry points
# Use the len() function
if len(job_wage) > 0 and len(job_area):

    try:
        # Check if the user entered numeric input for the wage part
        wage_final = int(job_wage)

        # determine the output depending on the location and the respective wages
        # Using the title() function;
        # we convert the entered text to lower case with the first character in caps (Capital Letter)
        if job_area.title() == "Mbarara" and wage_final > 4000000:
            print("Without a doubt, i will take it!")
        else:
            if job_area.title() == "Mbarara" and wage_final <= 4000000:
                print("No Thanks, I can find something better’")
            else:
                if job_area.title() == "Kampala" and wage_final >= 10000000:
                    print("Without a doubt, i will take it!")
                else:
                    if job_area.title() == "Kampala" and wage_final < 10000000:
                        print("No way!")
                    else:
                        if (job_area.title() != "Mbarara" and job_area.title() != "kampala" and job_area.title() != "Space") and wage_final >= 6000000:
                            print("Sure, I can work with this’")
                        else:
                            if (job_area.title() != "Mbarara" and job_area.title() != "kampala" and job_area.title() != "Space") and wage_final < 6000000:
                                print("No Thanks, I can find something better")
                            else:
                                if job_area.title() == "Space" and wage_final >= 0:
                                    print("Without doubt, i will take it")
    except:
        print("Error , enter numeric data for the wage part and try again!")
else:
    print("Please Enter the required Fields and try again!")