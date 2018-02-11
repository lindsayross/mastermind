import random

# create dictionary of colors
color_dict = {}
color_dict[1] = 'r'
color_dict[2] = 'o'
color_dict[3] = 'y'
color_dict[4] = 'g'
color_dict[5] = 'b'
color_dict[6] = 'p'

# generate random string of colors
pegs = ''
for i in range(4):           
    random_num = random.randint(1,6)
    random_color = color_dict[random_num]
    pegs += random_color

user_guess = input("Please make a guess of the colored pegs")
guess_count = 0
[b,w] = check_guess(user_guess, pegs)
print([b,w])
    
    

