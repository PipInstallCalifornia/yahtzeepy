import random
import time

'''
Global Variables Decloration

--- change to non global var, return at function 
--- explore new options for hoisting data
'''
global player_hand # list
global player_hand_counted # list
global dealer_hand # list
global dealer_hand_counted # list

# Declare variables to empty list
player_hand = []
player_hand_counted = []
dealer_hand = []
dealer_hand_counted = []

'''
End Global Variable Decloration
'''

'''
Start Generate Hand Logic
'''
# Move to pi randomization
# append all permutations to 
# list, select random 4 digits
# from pi less than than 6^5 + 1
# use index to select
# hand value
def generate_random_int():
    return random.randint(1,6) # int

def generate_random_hand():
    hand_list = []
    for x in range(5):
        x # do nothing excuse lint error
        hand_list.append(generate_random_int())
    return hand_list # list

'''
End Generate Hand Logic
'''


'''
Call to generated_random_hand() 
Generate Both Hands
'''
def get_player_hand():
    global player_hand
    player_hand = generate_random_hand() # list

def get_dealer_hand():
    global dealer_hand
    dealer_hand = generate_random_hand() # list

def get_both_hands():
    get_player_hand()
    get_dealer_hand()

'''
End Generate Both Hands
'''

'''
Start Occurence Counting Logic
'''
# Example: [1,3,4,2,2] returns
# [1,2,1,1,0] for list order
# [1,2,3,4,5] 
def count_number_occurences(hand):
    occurences_list = []
    for x in range(1,7):
        occurences = hand.count(x)
        occurences_list.append(occurences)
    return occurences_list

# Count occurences in both 
# player_hand, and dealer_hand
def count_player_hand(hand):
    global player_hand_counted
    occurences = count_number_occurences(hand) # yeilds list
    player_hand_counted = occurences

def count_dealer_hand(hand):
    global dealer_hand_counted
    occurences = count_number_occurences(hand) # yeilds list
    dealer_hand_counted = occurences

def count_both_hands():
    global player_hand
    global dealer_hand
    count_player_hand(player_hand)
    count_dealer_hand(dealer_hand)

'''
End Occurence Counting Logic
'''

'''
Start Hand Strength Evaluation Logic
'''
# Takes in [0,0,2,0,0], 2 returns int 3
# Can take in multiple occurence values 
# Usage: index_value(occurences_list, [3,2])
# Returns list, ex: [2], [2,5]
def index_value(occurences_list, occurences):
    index_list = []
    for occurence in occurences:
        try:
            if len(index_list) == 2:
                break
            index = occurences_list.index(occurence)
            occurences_list[index] = 0
            occurence_number = index + 1
            index_list.append(occurence_number)
        except:
            break
    print(index_list)
    if index_list:
        return index_list
    else:
        return False

def straight_power(occurences_list):
    if occurences_list == [1,1,1,1,1,0]:
        return [1] # purposely a list to remain consistent with index_value
    if occurences_list == [0,1,1,1,1,1]:
        return [2]
    else:
        return False

# Determine whole number power, append prefixed
# to suffix value as a float to help
# compare dealer hand to players 

def create_float(whole_number_value, suffix_list):
    stringed_value = "."
    if whole_number_value != 6: # don't sort value if full house
        suffix_list.sort(reverse=True)
    for suffix in suffix_list:
        stringed_value += str(suffix)
    unstringed_value = float(stringed_value[0:3])
    float_value = whole_number_value+unstringed_value
    return float_value

def evaluate_5_of_a_kind(occurences_list):
    if 5 in occurences_list:
        return (True, 7)
    else:
        return False

def evaluate_full_house(occurences_list):
    if 3 in occurences_list and 2 in occurences_list:
        return (True, 6)
    else:
        return False

def evaluate_4_of_a_kind(occurences_list):
    if 4 in occurences_list:
        return (True, 5)
    else:
        return False

def evaluate_straight(occurences_list):
    is_a_straight = False 
    if occurences_list == [1,1,1,1,1,0]:
        is_a_straight = True
    if occurences_list == [0,1,1,1,1,1]:
        is_a_straight = True
    if is_a_straight:
        return (True, 4)
    else:
        return False

def evaluate_3_of_a_kind(occurences_list):
    if 3 in occurences_list:
        return (True, 3)
    else:
        return False

def evaluate_2_pair(occurences_list):
    pair_count = 0
    for occurence in occurences_list:
        if occurence == 2:
            pair_count += 1
    if pair_count == 2:
        return (True, 2)
    else:
        return False

def evaluate_pair(occurences_list):
    if 2 in occurences_list:
        return (True, 1)
    else:
        return False

def evaluation_function(occurences_list):
    # consider a case switch
    # refinement needed
    if evaluate_5_of_a_kind(occurences_list):
        return create_float(7,
        index_value(occurences_list, [5]))

    elif evaluate_full_house(occurences_list):
        # create argument to put 3 of a kind value first
        return create_float(6, 
        index_value(occurences_list, [3,2]))

    elif evaluate_4_of_a_kind(occurences_list):
        return create_float(5, 
        index_value(occurences_list, [4]))

    elif evaluate_straight(occurences_list):
                                  # try to reduce line length to pound sign
        return create_float(4, 
        straight_power(occurences_list))

    elif evaluate_3_of_a_kind(occurences_list):
        return create_float(3, 
        index_value(occurences_list, [3]))
    # needs testing
    elif evaluate_2_pair(occurences_list):
        return create_float(2, 
        index_value(occurences_list, [2,2]))

    elif evaluate_pair(occurences_list):
        return create_float(1, 
        index_value(occurences_list, [2]))

    else:
        return 0.0

'''
End Hand Strength Evaluation Logic
'''

'''
Start Gameloop
'''


'''
End Gameloop
'''