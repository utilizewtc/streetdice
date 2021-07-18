from random import randint


def roll_prompt():
    roll_call = input("(R)oll the Dice, (E)xit the game: ")
    while roll_call.lower() not in ['r', 'e']:
        print("Input incorrect, please try again.")
        roll_call = input("(R)oll the Dice, (E)xit the game: ")
    if roll_call.lower() == 'r':
        roll_total = roll_the_dice()
    elif roll_call.lower() == 'e':
        print("Thank you for playing, try your luck again soon!")
        exit()
    return roll_total


def roll_the_dice():
    die_1, die_2 = randint(1, 6), randint(1, 6)
    die_total = die_1 + die_2
    print("")
    print("First Die:", die_1, "Second Die:", die_2)
    print("")
    print("You have rolled a", die_total)
    print("")
    return die_total

def gameplay():
    current_total = roll_prompt()
    if pass_status.lower() == 'p':
        if current_total in pass_set:
            print("You have won!")
        elif current_total in dont_pass_set:
            print("You have lost!")
        elif current_total not in pass_set or current_total not in dont_pass_set:
            print("The point is", current_total)
            point = current_total
            point_compare = roll_prompt()
            if point_compare != point:      
                while point_compare != point and point_compare != 7:
                    print("The point is", point)
                    point_compare = roll_prompt()
                if point_compare == 7:
                    print("You have lost!") 
            if point_compare == point:
                            print ("You have won!")
    elif pass_status.lower() == 'd':
        if current_total in dont_pass_set:
            print("You have won!")
        elif current_total in pass_set:
            print("You have lost!")
        elif current_total not in pass_set or current_total not in dont_pass_set:
            point = current_total
            print("The point is", current_total)
            point_compare = roll_prompt()
            if point_compare != point:      
                while point_compare != point and point_compare != 7:
                    point_compare = roll_prompt()
                if point_compare == 7:
                    print("You have won!") 
            if point_compare == point:
                            print ("You have lost!")


def pass_or_exit():
    pass_option = input("(P)ass, (D)on't Pass, or (E)xit ")
    while pass_option.lower() not in ['p', 'd', 'e']:
        print("Input incorrect, please try again.")
        pass_option = input("(P)ass or (D)on't, or (E)xit ")
    if pass_option.lower() == 'e':
        print("Thank you for playing, try your luck again soon!")
    return pass_option


pass_set = {7, 11}
dont_pass_set = {2, 3, 12}

pass_status = pass_or_exit()
while pass_status.lower() in ['p', 'd']:
    gameplay()
    pass_status = pass_or_exit()
if pass_status.lower() == 'e':
    exit()