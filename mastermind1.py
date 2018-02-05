import re
colors = set('roygbp')
feedbacks = set('10')

#Function that would print instruction for the player
def instruction():
	print("blah blah blah")
	go_back_button = str(input("Press 1 to go back to the menu\n"))
	
	while go_back_button != "1":
		print("blah blah blah")
		go_back_button = str(input("Press 1 to go back to the menu\n"))
	if go_back_button == "1":
		main()
		
#Codes for code breaker go to this function
def code_breaker():
	print("test code_break")
	return;

#Function for score, 4 variables will be passed in, variable guess_count is number of guess user or computer use
#variable guesses is the total guesses for each game mode
#variable mode is either 1 or 2, 1 for code_maker and 2 for code_breaker
#variable cheat_bool to check if player cheat or not, only for code_maker
def score(guess_count, guesses, mode, cheat_bool):
	if mode == 1:
		if(guess_count > 1 and guess_count <= guesses):
			print("The Computer won!")
			print("The Computer's score is:", guess_count,"guesses out of ",guesses,"total guesses!")
		elif(guess_count == 1):
			print("The Computer won")
			print("The Computer's score is:", guess_count,"guesses out of ",guesses,"total guesses!")
		else:
			if(cheat_bool == False):
				print("You won!")
			else:
				print("You won! But we know you cheated >:)\n")
	if mode == 2:
		if(guess_count > 1 and guess_count <= guesses):
			print("You won!")
			print("Your score is:", guess_count,"guesses out of ",guesses,"total guesses!")
		elif(guess_count == 1):
			print("You won!")
			print("Your score is:", guess_count,"guess out of ",guesses,"total guesses!")
		else:
			print("You lost!")
	return;	
			
#Function that returns number of guesses for each game mode
def game_mode_guess(game_mode):
	guesses = 7
	if int(game_mode) == 1:
		guesses = 7
	if int(game_mode) == 2:
		guesses = 5
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
		if any((i not in colors) for i in user_color):
			user_color_check = False
	else:
		user_color_check = False
	
	return user_color_check

#Check user feedback to make sure that its a number either 1 or 0 and its not any other char
#Return a boolean value
def user_feedback_cheking(user_feedback):
	user_feedback_check = True
	if user_feedback.isdigit() == True and len(user_feedback) <= 4:
		user_feedback_check = True
		if any((i not in feedbacks) for i in user_feedback):
			user_feedback_check = False
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
	user_color = input("Please choose your colors: ")
	user_color_check = user_color_checking(user_color)
	while user_color_check == False:
		user_color = input("Please choose your colors: ")
		user_color_check = user_color_checking(user_color)
	
	user_feedback = input("Pleas provide feedback either 1 or 0: ")
	user_feedback_check = user_feedback_cheking(user_feedback)
	while user_feedback_check == False:
		user_feedback = input("Pleas provide feedback either 1 or 0: ")
		user_feedback_check = user_feedback_cheking(user_feedback)
		
	print("test code_maker")
	return;

#This function is only for testing; therefore, I will not put any input check into it :)
def unit_test():
	test_mode = int(input("Press 1 to test score\n"))
	
	while test_mode != 1:
		test_mode = str(input("Press 1 to test score\nPress 2 to test game_mode\n"))
	if test_mode == 1:
		guesses = int(input("Total guesses: "))
		guess_count = int(input("Guess count: "))
		mode = int(input("Mode: "))
		cheat_input = int(input("Cheat (1 = True, 0 = False: "))
		cheat_bool = False
		if cheat_input == 1:
			cheat_bool = True
		else:
			cheat_bool = False
		score(guess_count, guesses, mode, cheat_bool)
	
	return;	
def main():
	print("Welcome to Mastermind!")
	mode = str(input("Press 1 to play in code-maker mode \nPress 2 to play in code-breaker mode\nPress 3 for instruction\nPress 4 for unit test\n" ))

	#Loop until user give the right input
	while mode != "1":
		if mode == "2":
			break
		if mode == "3":
			break
		if mode == "4":
			break
		mode = str(input("Press 1 to play in code-maker mode \nPress 2 to play in code-breaker mode\n" ))
	
	#Switch case for mode
	if mode == "1":
		code_maker()
	elif mode == "2":
		code_breaker()
	elif mode == "3":
		instruction()
	elif mode == "4":
		unit_test()
		
main()
