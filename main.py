## This program intends to calculate the user's weighted and unweighted grade-point-average.
## It prompts the user for their class name, class rigor-level, and class grade, in order to calculate the GPAs.
## The program assumes that the weighted GPA's factor by which it is added is 0.5 for honors-level classes and 1 for AP-level class.
## If a user enters an invalid input, the program allows the user to try again until the input is valid.
import sys
import statistics

weighted_gpa_list = []
unweighted_gpa_list = []
honors_factor = 0.5
ap_factor = 1

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
  
def calculate_weighted(gpa, rigor):
  if rigor == "Regular":
    return gpa
  elif rigor == "Honors":
    weighted_gpa = gpa + honors_factor
    return weighted_gpa
  elif rigor == "AP":
    weighted_gpa = gpa + ap_factor
    return weighted_gpa

number_of_subjects = False
print("Hello there! Would you like to calculate your grade-point-average?")
reply_to_prompt = input("Reply 'Yes' if you do, or 'No' if you do not: ")

if not "y" in reply_to_prompt.lower():
  sys.exit("The user did not wish to continue with the program.")

print("Please respond to the questions in the answer-format associated with that question!")

while not number_of_subjects:
  user_response = input("How many subjects do you have?: ")
  if user_response.isdigit():
    number_of_subjects = int(user_response)
  else:
    print("Your response was invalid. Please try again.")


for class_count in range(number_of_subjects):
  class_rigor = False
  class_grade = False
  class_name = False

  if class_count == 0: 
    print("Alright, let's start with the data for your first class!")
  else:
    print("Let's continue to the next class!")

  while not class_name:
    user_response = input("Please enter the name of your current class: ")
    if isinstance(user_response, str):
      class_name = user_response
    else:
      print("Your response was invalid. Please try again.")

  print("What rigor-level is the class '" + class_name + "'? Is it Regular, Honors, GT, OnRamps, or AP?")
  print("If you have an a class that is both AP & GT or AP & OnRamps, just respond with 'AP' for the level of your class.")
  print("If this is left blank, it will be considered a regular class.")

  while not class_rigor:
    user_response = input("Please enter your class rigor-level here: ").lower()
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
      print("Your response was invalid. Please try again.")
      continue
      

  while not class_grade:
    user_response = input("What is your grade, from 0-100, in the class '" + class_name + "'?: ")
    if user_response.isdigit():
      int_input = int(user_response)
      if int_input >= 0 and int_input <= 100:
        class_grade = int_input
        break
    print("Your response was invalid. Please try again.")

  class_grade = float(calculate_unweighted(class_grade))
  class_weighted_grade = float(calculate_weighted(class_grade, class_rigor))
  unweighted_gpa_list.append(class_grade)
  weighted_gpa_list.append(class_weighted_grade)

unweighted_gpa = round(statistics.mean(unweighted_gpa_list), 2)
weighted_gpa = round(statistics.mean(weighted_gpa_list), 2)
print("I appreciate all that data. Please give me a moment to calculate your unweighted grade-point-average.")
print("Your unweighted GPA is a " + str(unweighted_gpa))
print("And, your weighted GPA is a " + str(weighted_gpa))
