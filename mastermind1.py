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

#Check user feedback to make sure that its a number and it is less than the code length.
#Return a boolean value
def user_feedback_checking(user_feedback, code_length):
	user_feedback_check = True
	if user_feedback.isdigit() == True and int(user_feedback) <= code_length:
		user_feedback_check = True
	else:
		user_feedback_check = False
	
	return user_feedback_check

#This method takes a code and a guess as string arguments and determines the
#key pegs (black for correct color in correct position, white for correct color
#in incorrect position) that should be returned to the user as feeback for
#their guess in the code-breaker mode. Also used in the algorithm that chooses
#the next guess in the code-maker mode. Returns tuple of black and white pegs.
def check_guess(guess, code):
        black = 0 #number of correct colors in correct positions
        white = 0 #number of correct colors in wrong positions
        guess_remain = [] #list of guess pegs that did not earn a black key-to check for white
        code_remain = [] #list of code pegs that were not guessed in the correct position

        for g, c in zip(guess, code):
                if g == c:
                        black += 1 #item in guess is in same position as in code
                else:
                        guess_remain.append(g)
                        code_remain.append(c)
        for g in guess_remain:
                try:
                        code_remain.remove(g) #if there is a match, remove the item from the
                                   #code_remain list so it cannot be matched again in error
                        white += 1 #item in guess is the correct color, but in the wrong position
                except ValueError:
                        True
        return [black, white]

#Creates list of possible solutions used to choose the computer's next guess
#in the code-maker mode. Takes the string of the set of codes and the code length
#as arguments and returns a list of possible solutions.
def initialize_possible_solution_list(set_of_codes, code_length):
        number_of_codes = len(set_of_codes)
        index = [0]*code_length
        possible_solutions = []
        number_possible_solutions = number_of_codes**code_length
        for i in range(number_possible_solutions):
                solution = ""
                for j in range(code_length):
                        solution = set_of_codes[index[j]] + solution #build each possible solution peg by peg 
                possible_solutions.append(solution) #add possible solution to list of possible solutions
                for k in range(code_length):
                        index[k] += 1 #increment index of code
                        if index[k] == number_of_codes:
                                index[k] = 0 #roll over code index
                        else:
                                break
        return possible_solutions

#Removes items from the computer's list of possible solutions for the code-maker mode.
#Takes the list of possible solutions, the feedback keys provided by the user, and the
#guess as arguments and returns the list of possible solutions (now reduced).
def remove_solutions (possible_solutions, keys, guess):
        bad_solutions = []
        for solution in possible_solutions:
                if check_guess(solution, guess) != keys:
                        bad_solutions.append(solution) #Remove all possible solutions that would not give
                                #the same score of colored and white pegs if they were the answer. 
        for item in bad_solutions:
                possible_solutions.remove(item)#remove bad_solutions from possible_solutions list
        return possible_solutions

#Finds the computer's next guess. Takes the list of unguessed options and the current list of
#possible solutions as arguments and returns the next guess. For each unguessed option, it calculates
#how many possible solutions would be eliminated for each possible colored/white peg score. The score
#of a guess is the least of such values.
def find_next_guess(unguessed_options, possible_solutions, code_length):
        num_remain_in_possible_solutions = []
        for option in unguessed_options: #For each unguessed option, calculate how many possibile solutions
                                #would be eliminated for each possible key score
                score_list = []
                for i in range(code_length + 1):
                        score_list.append([0]*(code_length + 1))
                for solution in possible_solutions:
                    keys = check_guess(solution, option)
                    score_list[keys[0]][keys[1]] = score_list[keys[0]][keys[1]] + 1
                num_remain_in_possible_solutions.append(max(sum(score_list, [])))
        min_number = min(num_remain_in_possible_solutions)
        min_found = False
        next_guess = ""
        for i in range(len(unguessed_options)):
                if num_remain_in_possible_solutions[i] == min_number:
                        if (unguessed_options[i] in possible_solutions):
                                next_guess = unguessed_options[i]
                                break
                elif(not min_found):
                        next_guess = unguessed_options[i]
                        min_found = True               
        return next_guess

#Codes for code maker go to this function
def code_maker():
	game_mode = str(input("\nPlease choose a game mode:\nPress 1 for easy\nPress 2 for medium\nPress 3 for hard\n"))
	game_mode_check = game_mode_checking(game_mode)
	while game_mode_check == False:
		game_mode = str(input("Try again. Please choose a game mode:\nPress 1 for easy\nPress 2 for medium\nPress 3 for hard\n"))
		game_mode_check = game_mode_checking(game_mode)
	
	number_of_guesses = game_mode_guess(game_mode)
	print("\nThe computer will get", number_of_guesses, "guesses.")
	user_code = str(input("\nPlease choose your colors: "))
	user_color_check = user_color_checking(user_code)
	while user_color_check == False:
		user_code = str(input("Try again. Please choose your colors: "))
		user_color_check = user_color_checking(user_code)

	string_of_codes = "roygbp"
	code_length = 4
	possible_solutions = initialize_possible_solution_list(string_of_codes, code_length)
	unguessed_options = list(possible_solutions)
	initial_guess = "rroo"
	current_guess = initial_guess
	solved = False
	cheated = False

	for attempt in range(number_of_guesses):
		if possible_solutions != []:
			print("\nComputer's guess " + str(attempt + 1) + ":", current_guess)
			unguessed_options.remove(current_guess)
		else:
			possible_solutions = initialize_possible_solution_list(string_of_codes, code_length)
			unguessed_options = list(possible_solutions)
			current_guess = initial_guess
			print("\nComputer's guess " + str(attempt + 1) + ":", current_guess)
			unguessed_options.remove(current_guess)

		user_feedback_black = str(input("How many black keys does this guess get?"))
		user_feedback_black_check = user_feedback_checking(user_feedback_black, code_length)
		while user_feedback_black_check == False:
			user_feedback_black = str(input("Try again. How many black keys does this guess get?"))
			user_feedback_black_check = user_feedback_checking(user_feedback_black, code_length)

		user_feedback_white = str(input("How many white keys does this guess get?"))
		user_feedback_white_check = user_feedback_checking(user_feedback_white, code_length)
		while user_feedback_white_check == False:
			user_feedback_white = str(input("Try again. How many white keys does this guess get?"))
			user_feedback_white_check = user_feedback_checking(user_feedback_white, code_length)

		user_keys = [int(user_feedback_black), int(user_feedback_white)]
		keys = check_guess(current_guess, user_code)#to be replaced with or compared to user feedback
							#--currently compared to check for cheating
		print("User response:", user_keys) #first element is black pegs, second is white
		print("Actual response:", keys)

		if user_keys != keys:
			cheated = True

		if user_keys[0] == code_length:
			solved = True
			break

		possible_solutions = remove_solutions(possible_solutions, user_keys, current_guess)
		print(possible_solutions)
		current_guess = find_next_guess(unguessed_options, possible_solutions, code_length)
		print(current_guess)
	if solved == True:
		print("\nComputer won with", attempt + 1, "guesses!")
		if cheated == True:
			print("(But we know you cheated!!)")
	if solved == False:
		print("\nYou won! The computer could not solve your code in", attempt +1, "guesses.")
		if cheated == True:
			print("(But we know you cheated!!)")

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
