## This program intends to calculate the user's weighted and unweighted grade-point-average.
## It prompts the user for their class name, class rigor-level, and class grade, in order to calculate the GPAs.
## The program assumes that the weighted GPA's factor by which it is added is 0.5 for honors-level classes and 1 for AP-level class.
## If a user enters an invalid input, the program allows the user to try again until the input is valid.
import sys
import statistics
import time

## Variables are declared below
time_to_read = 1 ## Time between each print statement, to give the user time to read the instructions
weighted_gpa_list = [] ## Table that will contain the user's weighted grade-point-averages
unweighted_gpa_list = [] ## Table that will contain the user's unweighted grade-point averages
honors_factor = 0.5 ## Factor by which the grade-point-average of Honors-level classes increases
ap_factor = 1 ## Factor by which the grade-point-average of AP-level classes increases

## This function calculates the unweighted grade-point-average of the user based on a scale
def calculate_unweighted(grade):
  if grade >= 93:
    return 4.0
  elif grade >= 90:
    return 3.7
  elif grade >= 87:
    return 3.3
  elif grade >= 83:
    return 3.0
  elif grade >= 80:
    return 2.7
  elif grade >= 77:
    return 2.3
  elif grade >= 73:
    return 2.0
  elif grade >= 70:
    return 1.7
  elif grade >= 67:
    return 1.3
  elif grade >= 65:
    return 1.0
  else:
    return 0.0

## This function calculates the user's weighted grade-point-average, by taking the unweighted GPA and adding the weighted factor for the associated class's rigor level
def calculate_weighted(gpa, rigor):
  if rigor == "Regular":
    return gpa
  elif rigor == "Honors":
    weighted_gpa = gpa + honors_factor
    return weighted_gpa
  elif rigor == "AP":
    weighted_gpa = gpa + ap_factor
    return weighted_gpa

number_of_subjects = False ## The default value of this is false; will be explained more as we progress through the code
print("Hello there! Would you like to calculate your grade-point-average?")
reply_to_prompt = input("Reply 'Yes' if you do, or 'No' if you do not: ")

if not "y" in reply_to_prompt.lower(): ## If the user has the character "y" anywhere in the response, the program will continue
  sys.exit("The user did not wish to continue with the program.")

print("Please respond to the questions in the answer-format associated with that question!")
time.sleep(time_to_read)

while not number_of_subjects: ## Loop keeps going until number_of_subjects is not equal to False
  user_response = input("How many subjects do you have?: ")
  if user_response.isdigit():
    number_of_subjects = int(user_response) ## If the user response is valid, the variable is set to an integer conversion of the user response
  else:
    print("Your response was invalid. Please try again.") ## If the user response is invalid, the variable is still False and the loop continues

## The loop below loops through each subject to get the data for the subject
for class_count in range(number_of_subjects):
  ## Declaring more variables that reset everytime the loop begins a cycle
  class_rigor = False ## This variable will hold the rigor-level of the class, so we can see what factor the weighted grade-point-average of said class increases by
  class_grade = False ## This variable holds the unweighted grade of the class, from 1-100
  class_name = False ## This variable holds the name of the class

  if class_count == 0: ## If it's the first cycle of the loop, this statement prints
    print("Alright, let's start with the data for your first class!") 
  else: ## If it's not the first cycle of the loop, this statement prints
    print("Let's continue to the next class!")

  time.sleep(time_to_read)
  while not class_name: ## Loop keeps going until class_name is not False
    user_response = input("Please enter the name of your current class: ")
    if isinstance(user_response, str):
      class_name = user_response ## If the user response is a string, the class_name variable is set to the user_response variable and we exit the loop since class_name is not false anymore
    else:
      print("Your response was invalid. Please try again.") ## If the user response is invalid, the variable is still False and the loop continues

  print("What rigor-level is the class '" + class_name + "'? Is it Regular, Honors, GT, OnRamps, or AP?")
  time.sleep(time_to_read)
  print("If you have an a class that is both AP & GT or AP & OnRamps, just respond with 'AP' for the level of your class.")
  time.sleep(time_to_read)
  print("If this is left blank, it will be considered a regular class.")
  time.sleep(time_to_read)

  while not class_rigor: ## Keeps looping until class_rigor is not False
    user_response = input("Please enter your class rigor-level here: ").lower() ## Gets the lowercase string of the user_response
    if user_response == "regular" or user_response == "":
      class_rigor = "Regular"
    elif user_response == "honors":
      class_rigor = "Honors"
    elif user_response == "gt":
      class_rigor = "Honors"
    elif user_response == "onramps" or user_response == "on-ramps" or user_response == "on ramps":
      class_rigor = "Honors"
    elif user_response == "ap":
      class_rigor = "AP"
    else:
      print("Your response was invalid. Please try again.") ## If the user response meets none of the conditions above, the loop continues as class_rigor is still False
      
  time.sleep(time_to_read)
  while not class_grade: ## This loop keeps looping until class_grade is not False 
    user_response = input("What is your grade, from 0-100, in the class '" + class_name + "'?: ")
    if user_response.isdigit(): ## Checking if the user response is a digit
      int_input = int(user_response) ## The string returned from the user_response variable is converted to an integer value and stored in int_input
      if int_input >= 0 and int_input <= 100: ## Checking if the user response is between 1 and 100 (included)
        class_grade = int_input ## The class_grade variable is set equal to the int_input variable if all the conditions are met
        break ## If user response passes all the checks, we exit the loop through the 'break' keyword
    print("Your response was invalid. Please try again.")

  class_grade = float(calculate_unweighted(class_grade)) ## We convert the class_grade value to a scaled grade-point-average, on the 4.0 scale, through the calulate_unweighted() function
  class_weighted_grade = float(calculate_weighted(class_grade, class_rigor)) ## We convert the scaled class_weighted_grade grade-point-average, on the 4.0 scale, to a weighted GPA, on the 5.0 scale, through the calculate_weighted() function 
  unweighted_gpa_list.append(class_grade) ## We add the calculated unweighted grade-point-average of said class to the unweighted_gpa_list
  weighted_gpa_list.append(class_weighted_grade) ## We add the calculated weighted grade-point-average of said class to the weighted_gpa_list

## After the loop loops through all the subjects, it is over and the code proceeds
unweighted_gpa = round(statistics.mean(unweighted_gpa_list), 2) ## The unweighted_gpa is calulated by finding the mean/average of the unweighted_gpa_list
weighted_gpa = round(statistics.mean(weighted_gpa_list), 2) ## The weighted_gpa is calculated by find the mean/average of the weighted_gpa_list
print("I appreciate all that data. Please give me a moment to calculate your unweighted grade-point-average.")
time.sleep(time_to_read)
## Both grade-point-averages are displayed to the user below
print("Your unweighted GPA is a " + str(unweighted_gpa))
print("And, your weighted GPA is a " + str(weighted_gpa))
