# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    ...


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    ...


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    ...


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    ...


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    ...


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    ...


if __name__ == "__main__":
    main()
