import re
print("Welcome to Mastermind!")

mode = str(input("Press 1 to play in code-maker mode \nPress 2 to play in code-breaker mode\n" ))

#Loop until user give the right input
while mode != "1":
	if mode == "2":
		break
	mode = str(input("Press 1 to play in code-maker mode \nPress 2 to play in code-breaker mode\n" ))

#Codes for code breaker go to this function
def code_breaker():
	print("test code_break")
	return;

#Check function make sure that input is a number and is less than 6
#Return a boolean value
def length_checking(length):
	length_check = True
	if length.isdigit() == True and int(length) <= 4:
		length_check = True
	else:
		length_check = False
	return length_check

#Check function make sure that input is a number and is less than 12
#Return a boolean value
def number_checking(number_guess):
	number_check = True;
	if number_guess.isdigit() == True and int(number_guess) <= 12:
		number_check = True
	else:
		number_check = False
	return number_check
	
#Check user input to make sure if its a string, correct length and not out of bound from a - file
#Return a boolean value
def user_color_checking(user_color, length):
	user_color_check = True
	if user_color.isdigit() == False and len(user_color) == int(length):
		user_color_check = True
		if any( [i<'a' or i>'f' for i in user_color]):
			user_color_check = False
	else:
		user_color_check = False
	
	return user_color_check

#Check user feedback to make sure that its a number either 1 or 0 and its not any other char
#Return a boolean value
def user_feedback_cheking(user_feedback):
	user_feedback_check = True
	if user_feedback.isdigit() == True and len(user_feedback) == 1 and any( [int(i)==0 or int(i)==1 for i in user_feedback]):
		user_feedback_check = True
	else:
		user_feedback_check = False
	
	return user_feedback_check
	
#Codes for code maker go to this function
def code_maker():
	length = input("Please choose number of color from 1 - 4: ")
	length_check = length_checking(length)
	
	while length_check == False:
		length = input("Please choose number of color from 1 - 4: ")
		length_check = length_checking(length)
	
	number_guess = input("Please choose number of guesses 1 - 12: ")
	number_check = number_checking(number_guess)
	while number_check == False:
		number_guess = input("Please choose number of guesses 1 - 12: ")
		number_check = number_checking(number_guess)
	
	user_color = input("Please choose color from a-f: ")
	user_color_check = user_color_checking(user_color, length)
	while user_color_check == False:
		user_color = input("Please choose color from a-f: ")
		user_color_check = user_color_checking(user_color, length)
	
	user_feedback = input("Pleas provide feedback either 1 or 0: ")
	user_feedback_check = user_feedback_cheking(user_feedback)
	while user_feedback_check == False:
		user_feedback = input("Pleas provide feedback either 1 or 0: ")
		user_feedback_check = user_feedback_cheking(user_feedback)
		
	print("test code_maker")
	return;

#Switch case for mode
if mode == "1":
	code_maker()
elif mode == "2":
	code_breaker()
