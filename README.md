# Fork & Clone

Fork and clone [this repository](https://github.com/JoinCODED/recruitment) in your `python` directory.

---

# Task 

In this task you'll be creating a recruitment system. You'll ask the user a few questions and depending on their answers you will either accept or reject the applicant.

Example:

```
Welcome to the special recruitment program, please answer the following questions:
What's your name? Kale Salad
How old are you? 30
How many years of experience do you have? 6

Skills:
1. Python
2. C++
3. Javascript
4. Juggling
5. Running
6. Eating

Choose a skill from above by entering its number: 1
Choose another skill from above by entering its number: 6
You have been accepted, Kale Salad.
```

In this example, the user entered their name, age, years of experience, and chose the 1st and 6th skills from the list.

## Steps:

1. In the `get_skills` function, add at least 3 random skills to the list
2. In the `show_skills` function, print all the skills to the user, so that we can call this function before prompting the user to select from them.
    - The printed skills should be listed in a shape of an ordered list from 1 ... `n`, where n is the length of the list (look into `enumerate`).
3. In the `get_user_skills`, show the `skills` (received from the parameter) to the user. Prompt the user to select 2 `skills` and return the two `skills` the user selected in a list.
4. In `get_user_cv`:
    1. Create an empty dictionary called `cv`. This dictionary will then hold all of the applicant's information.
    2. Ask the users for their name. Save the name in the `cv` dictionary with key `name`.
    3. Ask the users for their age. Save the age in the `cv` dictionary with key `age`.
    4. Ask the users for their years of experience. Save the years of experience in the `cv` dictionary with key `experience`.
    5. Add a key called `skills`, and assign it to the output of `get_user_skills` function.
    6. Return the `cv` you have built thus far.
5. In `check_acceptance`, return `True` if their `age` is between `25` and `40`, they have more than `3` years of `experience`, and the `desired_skill` is within their `skills`.
6. In the `main` function:
    1. `print` a welcome message to this recruitment program.
    2. Get the list of `skills` using the `get_skills` function you created, and assign it to a variable called `skills`.
    3. Call the `get_user_cv` function, pass `skills` to it, and assign the result to a variable called `cv`.
    4. Check the applicant's acceptance using `check_acceptance`, and pass in two arguments: the cv and the 3rd `skill` from your list of `skills`, created in Step 2, as the "`desired_skill`".
    5. If the applicant has been accepted, print a message to the user saying they're accepted (make sure the word "accepted" appears in that message.) Otherwise, print another message saying to the user they weren't accepted (make sure the word "rejected" appears in this message.)

Hint: To check if an element exists in a list, go [here](https://www.w3schools.com/python/python_lists.asp) and scroll down to "_Check if Item Exists_".
