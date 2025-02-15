# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    skills = ["Boxing", "Reading", "Playing"]
    return skills

# print (get_skills())

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    for index, skill in enumerate(skills, 1):
        print (index, skill)

# show_skills (get_skills())






# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):

    show_skills (get_skills())  
    user_skill1 = int(input("Enter the number for your first skill"))
    user_skill2 = int(input("Enter the number for your second skill"))
    user_skills = [skills[user_skill1 - 1], skills[user_skill2 - 1]]
    return user_skills

    # for num in skills:
    #     if user_skill1 == num :
    #         print (f"") 
      
# print (get_user_skills(get_skills()))


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {}

    cv["name"] = input ("What is your name?")
    cv["age"] = int(input("How old are you?"))
    cv["years_experience"] = int(input("How many years of experience do you have?"))
    cv["skills"] = get_user_skills(skills)
    return cv

# print (get_user_cv())



    
    


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):

    if (25 <= cv["age"] <= 40 and (cv ["years_experience"] > 3) and (desired_skill in cv ["skills"])):
        return True
    else:
        return False



def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print ("Welcome to the special recruitment program, please answer the following questions:")
    skills = get_skills()
    user_cv = get_user_cv(skills)
    is_accepted = check_acceptance(user_cv,skills)
    if is_accepted: 
        print (f"Congrats {user_cv['name']} , you have been accepted!")
    else:
        print ("Try again some othertime")
    

if __name__ == "__main__":
    main()
