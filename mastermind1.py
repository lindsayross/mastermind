import re
import random
import sys
colors = set('roygbp')
feedbacks = set('10')

#Authors: Anh Phan & Lindsay Ross
#Function that would print instruction for the player
def instruction():
	print("blah blah blah")
	go_back_button = str(input("Press 1 to go back to the menu\n"))
	
	while go_back_button != "1":
		print("blah blah blah")
		go_back_button = str(input("Press 1 to go back to the menu\n"))
	if go_back_button == "1":
		main()

#Author: Lindsay Ross		
#Codes for code breaker go to this function
def code_breaker(mode):

	# create dictionary of colors
	color_dict = {}
	color_dict[1] = 'r'
	color_dict[2] = 'o'
	color_dict[3] = 'y'
	color_dict[4] = 'g'
	color_dict[5] = 'b'
	color_dict[6] = 'p'

	# boolean to check whether or not the user wants to continue 
	done_mode = False

        # counts number of hints user asks for
	hint_count = 0
	
	# generate random string of colors
	pegs = ''
	for i in range(4):           
	    random_num = random.randint(1,6)
	    random_color = color_dict[random_num]
	    pegs += random_color

	# user chooses a game mode which determines the number of guesses
	guess_diff = str(input("\nPlease choose a game mode:\nPress 1 for easy\nPress 2 for medium\nPress 3 for hard\n"))
	guess_diff_check = guess_diff_checking(guess_diff)
	while guess_diff_check == False:
		guess_diff = str(input("\nPlease choose a game mode:\nPress 1 for easy\nPress 2 for medium\nPress 3 for hard\n"))
		guess_diff_check = guess_diff_checking(guess_diff)
	number_of_guesses = guess_diff_guess(guess_diff, mode)
	print("\nYou will have", number_of_guesses, "guesses.")
	print("\n------------------- \nPeg Colors \nr - red \no - orange \ny - yellow \ng - green \nb - blue \np - purple \n")
	print("\nFeedback Colors \nblack - you have a peg that is the right color in the right place \nwhite - you have a peg that is the right color, but in the wrong place ")
	print("\n\n'quit' - enter at any time to quit")
	print("'hint' - enter once per game for a hint; you will lose a guess")
	print("'done' - enter at any time to give up and view solution \n-------------------")
	user_guess = input("\nPlease make a guess of the colored pegs: ")
	# check to make sure guesses are valid
	user_color_check = user_color_checking(user_guess)
	while user_color_check == False:
		if user_guess == 'hint':
			generate_hint(pegs)
			user_color_check = True
			hint_count += 1
		elif user_guess == 'done':
			print("Game Over")
			print("The correct solution was", pegs)
			done_mode = True
			user_color_check = True
		else:
			user_guess = str(input("Try again. Please choose your colors: "))
			user_color_check = user_color_checking(user_guess)
	
	guess_count = 1 # counts user guesses 
	black_pegs, white_pegs = check_guess(user_guess, pegs) # determines black and white pegs
	
	# keep guessing while user still has more guesses and has not reached the solution
	while guess_count < number_of_guesses and black_pegs != 4 and done_mode == False :
		if user_guess != 'hint':
			print(black_pegs, "black pegs, and", white_pegs, "white pegs")
		user_guess = input("\nPlease make another guess: ")
		black_pegs, white_pegs = check_guess(user_guess, pegs)
		# check to make sure guesses are valid
		user_color_check = user_color_checking(user_guess)
		while user_color_check == False:
			if user_guess == 'hint' and hint_count < 1:
				generate_hint(pegs)
				user_color_check = True
				hint_count += 1
			elif user_guess == 'done':
				print("Game Over")
				print("The correct solution was", pegs)
				done_mode = True
				user_color_check = True
			else:
				user_guess = str(input("Try again. Please choose your colors: "))
				black_pegs, white_pegs = check_guess(user_guess, pegs)
				user_color_check = user_color_checking(user_guess)
		guess_count +=1
	if black_pegs == 4:
		print("You guessed the correct solution in", guess_count, "guesses! You win!")
	elif guess_count == number_of_guesses:
		print("You ran out of guesses, the Computer wins.")
		print("The correct solution was", pegs)

#Author: Lindsay Ross
# Function that takes in solution and indicates to the user the value of a random peg
def generate_hint(pegs):
        
        # generate random function
        random_peg = random.randint(0,3)
        # indicate random peg 
        print("The color at position", random_peg+1 ,"is", pegs[random_peg])

        
#Author: Anh Phan
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
				print("You won! However, this may be a result of your incorrect feedback\n")
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

#Author: Anh Phan	
#Function that returns number of guesses for each game mode
def guess_diff_guess(guess_diff, mode):
	guesses = 7
	if int(guess_diff) == 1:
		if int(mode) == 1:
			guesses = 5
		elif int(mode) == 2:
			guesses = 10
	if int(guess_diff) == 2:
		if int(mode) == 1:
			guesses = 4
		elif int(mode) == 2:
			guesses = 7
	if int(guess_diff) == 3:
		if int(mode) == 1:
			guesses = 3
		if int(mode) == 2:
			guesses = 5
	return guesses

#Author: Anh Phan	
#Check function make sure that input is a number and is less than 4
#Return a boolean value
def guess_diff_checking(guess_diff):
	guess_diff_check = True;
	if guess_diff == 'quit' or guess_diff == 'Quit' or guess_diff == 'QUIT':
		sys.exit()
	if guess_diff.isdigit() == True and int(guess_diff) > 0 and int(guess_diff) < 4:
		guess_diff_check = True
	else:
		guess_diff_check = False
	return guess_diff_check

#Author: Anh Phan and Lindsay Ross
#Check user input to make sure if its a string, correct length and not out of bound from a - file
#Return a boolean value
def user_color_checking(user_color):
	user_color_check = True
	if user_color == 'quit' or user_color == 'Quit' or user_color == 'QUIT':
		sys.exit()
	if user_color.isdigit() == False and len(user_color) == 4:
		user_color_check = True
		if any((i not in colors) for i in user_color):
			user_color_check = False
	else:
		user_color_check = False
	
	return user_color_check

#Author: Anh Phan and Lindsay Ross
#Check user feedback to make sure that its a number and it is less than the code length.
#Return a boolean value
def user_feedback_checking(user_feedback, code_length):
	user_feedback_check = True
	if user_feedback == 'quit' or user_feedback == 'Quit' or user_feedback == 'QUIT':
		sys.exit()
	if user_feedback.isdigit() == True and int(user_feedback) <= code_length:
		user_feedback_check = True
	else:
		user_feedback_check = False
	
	return user_feedback_check

#Author: Kristin Mills
#This method takes a code and a guess as string arguments and determines the
#key pegs (black for correct color in correct position, white for correct color
#in incorrect position) that should be returned to the user as feedback for
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

#Author: Kristin Mills
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

#Author: Kristin Mills
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

#Author: Kristin Mills
#Finds the computer's next guess using the Knuth algorithm, which guarantees that the algorithm will
#solve the code in 5 guesses or less. Takes the list of unguessed options and the current list of
#possible solutions as arguments and returns the next guess. For each unguessed option, it calculates
#how many possible solutions would remain for each possible colored/white peg score and uses a minimax
#algorithm to find the next guess that will reduce the possible_solutions list by the greatest number.
def find_next_guess(unguessed_options, possible_solutions, code_length):
	num_remain_in_possible_solutions = []
	for option in unguessed_options: #For each unguessed option, calculate how many possibile solutions
				#would remain for each possible key score
		score_list = []
		for i in range(code_length + 1):
			score_list.append([0]*(code_length + 1))
		for solution in possible_solutions:
		    keys = check_guess(solution, option)
		    score_list[keys[0]][keys[1]] = score_list[keys[0]][keys[1]] + 1
		num_remain_in_possible_solutions.append(max(sum(score_list, []))) #Add the maximum key
				#score for each unguessed option to the list of how many would remain

	min_number = min(num_remain_in_possible_solutions) #find the minimum number in the list
	min_found = False
	next_guess = ""

	for i in range(len(unguessed_options)):
		if num_remain_in_possible_solutions[i] == min_number: #if the one with the min number 
				#is in list of possible solutions, choose that one. Otherwise, choose any
			if (unguessed_options[i] in possible_solutions):
				next_guess = unguessed_options[i]
				break
			elif(not min_found):
				next_guess = unguessed_options[i]
				min_found = True               
	return next_guess

#Authors: Anh Phan & Kristin Mills
#Codes for code maker go to this function
def code_maker(mode):
	guess_diff = str(input("\nPlease choose a game mode:\nPress 1 for hard\nPress 2 for medium\nPress 3 for easy\n"))
	guess_diff_check = guess_diff_checking(guess_diff)
	while guess_diff_check == False:
		guess_diff = str(input("Try again. Please choose a game mode:\nPress 1 for easy\nPress 2 for medium\nPress 3 for hard\n"))
		guess_diff_check = guess_diff_checking(guess_diff)
	
	number_of_guesses = guess_diff_guess(guess_diff, mode)
	print("\nThe computer will get", number_of_guesses, "guesses.")
	print("\n------------------- \nPeg Colors \nr - red \no - orange \ny - yellow \ng - green \nb - blue \np - purple \n")
	print("\nFeedback Colors \nblack - you have a peg that is the right color in the right place \nwhite - you have a peg that is the right color, but in the wrong place ")
	print("\n\n'quit' - enter at any time to quit\n-------------------")
	
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
			print("You colors are: " + user_code)
			unguessed_options.remove(current_guess)
		else:
			possible_solutions = initialize_possible_solution_list(string_of_codes, code_length)
			unguessed_options = list(possible_solutions)
			current_guess = initial_guess
			print("\nComputer's guess " + str(attempt + 1) + ":", current_guess)
			print("You colors are: " + user_code)
			unguessed_options.remove(current_guess)

		user_feedback_black = str(input("How many black keys does this guess get?"))
		user_feedback_black_check = user_feedback_checking(user_feedback_black, code_length)
		while user_feedback_black_check == False:
			user_feedback_black = str(input("Try again. How many black keys does this guess get?"))
			user_feedback_black_check = user_feedback_checking(user_feedback_black, code_length)

		user_feedback_white = str(input("How many white keys does this guess get?"))
		user_feedback_white_check = user_feedback_checking(user_feedback_white, code_length)
		user_feedback_total = int(user_feedback_black) + int(user_feedback_white)
		user_feedback_total_check = user_feedback_checking(str(user_feedback_total), code_length)

		while user_feedback_white_check == False or user_feedback_total_check == False :
			user_feedback_white = str(input("Try again. How many white keys does this guess get?"))
			user_feedback_white_check = user_feedback_checking(user_feedback_white, code_length)
			user_feedback_total = int(user_feedback_black) + int(user_feedback_white)
			user_feedback_total_check = user_feedback_checking(str(user_feedback_total), code_length)
			
		user_keys = [int(user_feedback_black), int(user_feedback_white)]
		keys = check_guess(current_guess, user_code)#compared to user feedback to check for wrong input
		print("User feedback:", user_keys) #first element is black pegs, second is white
		print("Correct feedback:", keys)

		if user_keys != keys:
			cheated = True

		if user_keys[0] == code_length:
			solved = True
			break

		possible_solutions = remove_solutions(possible_solutions, user_keys, current_guess)
		current_guess = find_next_guess(unguessed_options, possible_solutions, code_length)
		
	if solved == True:
		print("\nComputer won with", attempt + 1, "guesses!")
		if cheated == True:
			print("However, this result was due to your incorrect feedback")
	if solved == False:
		print("\nYou won! The computer could not solve your code in", attempt +1, "guesses.")
		if cheated == True:
			print("However, this result was due to your incorrect feedback")

	return;

#This function is only for testing; therefore, I will not put any input check into it :)
def unit_test():
	test_mode = int(input("Press 1 to test score\n"))
	
	while test_mode != 1:
		test_mode = str(input("Press 1 to test score\nPress 2 to test guess_diff\n"))
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

#Author: Anh Phan
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
		code_maker(mode)
	elif mode == "2":
		code_breaker(mode)
	elif mode == "3":
		instruction()
	elif mode == "4":
		unit_test()
		
main()
