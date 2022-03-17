# Treehouse Prerequisites:

Finish the following chapters/steps from [this course](https://teamtreehouse.com/library/introducing-lists) on treehouse:

- Chapter "**Meet Lists**": All steps
- Chapter "**Using Lists**": All steps

Finish the following chapters/steps from [this course](https://teamtreehouse.com/library/introducing-dictionaries) on treehouse:

- Chapter "**Introducing Dictionaries**": All steps

---

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

1. Create a list called `skills` and fill it with any skills of your choice. These are the skills that the user will choose from.
2. Create an empty dictionary called `cv`. This dictionary will then hold all of the applicant's information.
3. Ask the user for their name. Save the name in the `cv` dictionary with key `name`.
4. Ask the user for their age. Save the age in the `cv` dictionary with key `age`.
5. Ask the user for their years of experience. Save the years of experience in the `cv` dictionary with key `experience`.
6. Add a key `skills` to the `cv` dictionary and give it an empty list as a value.
7. Print the skills from the `skills` list and number them from 1. where 1 will have the first skill in the list (which has index 0).
8. Ask the user to choose a skill from the list. Then get the skill from the `skills` list and add it to the skills list in the `cv` dictionary.
    - For example, if the user enters 1, the skill "Python" should be added to the list `skills` in the dictionary `cv`.
9. Ask the user for another skill and add it to the skills list in the `cv` dictionary.
10. If the user's age is between 25 and 40, has over five years experience, and has the 6th skill from the skills list, print a message to the user saying they're accepted (make sure the word "accepted" appears in that message.) Otherwise, print another message saying to the user they weren't accepted (make sure the word "rejected" appears in this message.)

Hint: To check if an element exists in a list, go [here](https://www.w3schools.com/python/python_lists.asp) and scroll down to "_Check if Item Exists_".
