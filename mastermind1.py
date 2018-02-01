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

#Function that returns number of guesses for each game mode
def game_mode_guess(game_mode):
	guesses = 12
	if int(game_mode) == 1:
		guesses = 12
	if int(game_mode) == 2:
		guesses = 7
	if int(game_mode) == 3:
		guesses = 3
	return guesses
	
#Check function make sure that input is a number and is less than 12
#Return a boolean value
def game_mode_checking(game_mode):
	game_mode_check = True;
	if game_mode.isdigit() == True and int(game_mode) > 0 and int(game_mode) < 4:
		game_mode_check = True
	else:
		game_mode_check = False
	return game_mode_check
	
#Check user input to make sure if its a string, correct length and not out of bound from a - file
#Return a boolean value
def user_color_checking(user_color):
	user_color_check = True
	if user_color.isdigit() == False and len(user_color) == 4:
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
	if user_feedback.isdigit() == True and len(user_feedback) > 4 and any( [int(i)==0 or int(i)==1 for i in user_feedback]):
		user_feedback_check = True
	else:
		user_feedback_check = False
	
	return user_feedback_check
	
#Codes for code maker go to this function
def code_maker():
	game_mode = input("Please choose a game mode:\nPress 1 for easy\nPress 2 for medium\nPress 3 for hard\n")
	game_mode_check = game_mode_checking(game_mode)
	while game_mode_check == False:
		game_mode = input("Please choose a game mode:\nPress 1 for easy\nPress 2 for medium\nPress 3 for hard\n")
		game_mode_check = game_mode_checking(game_mode)
	
	guesses = game_mode_guess(game_mode)
	print(guesses)
	user_color = input("Please choose color from a-f: ")
	user_color_check = user_color_checking(user_color)
	while user_color_check == False:
		user_color = input("Please choose color from a-f: ")
		user_color_check = user_color_checking(user_color)
	
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
