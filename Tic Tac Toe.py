#!/usr/bin/env python
# coding: utf-8

# ## Tic Tac Toe!

# In[1]:


from IPython.display import clear_output
clear_output()


# my_dict = { 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
# position_list = list(range(1,10))
# game_round = 1

# In[2]:


def display_game(my_dict):
    

    print('Here is your current board')
    
    #print board as 3 parts
    print(' ', '|', ' ', '|', ' ')
    print(my_dict[7], '|', my_dict[8], '|', my_dict[9])
    print('_', '|', '_', '|', '_')
    
    print(' ', '|', ' ', '|', ' ')
    print(my_dict[4], '|', my_dict[5], '|', my_dict[6])
    print('_', '|', '_', '|', '_')
    
    print(' ', '|', ' ', '|', ' ')
    print(my_dict[1], '|', my_dict[2], '|', my_dict[3])
    print(' ', '|', ' ', '|', ' ')


# In[3]:


def position_choice(game_round):
    
    choice = 'wrong'
    acceptable_position = False
    
    #while choice is not a digit, keep asking for input
    while choice.isdigit() == False or acceptable_position == False:
        
        #taking input from player 1
        if game_round % 2 != 0:
            choice = input("Player 1 pick a poisiton between 1 to 9 to replace: ")
        
        else:
            choice = input("Player 2 pick a poisiton between 1 to 9 to replace: ")
        
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        
        if choice.isdigit() == True:
            
            #to check that position has not been picked before
            if int(choice) in position_list:
                acceptable_position = True
                # to remove choice from list of available positions
                position_list.remove(int(choice))
            
            #check if choice is within range
            elif int(choice) > 9 or int(choice) <1:
                within_range = False
                print("Sorry choice is out of range!")
            
            #check if choice has been chose before
            else:
                within_range = False
                print("Sorry position has been picked before!")
        
    return int(choice)


# In[4]:


def game_start():
    
    print('Welcome to Tic Tac Toe!')
    
    p1_marker = 'wrong'
    acceptable_input = ['X', 'O']
    
    # keep running for acceptable input
    while p1_marker not in ['X', 'O']:
        
        p1_marker = input('Player 1: Do you want to be X or O? ')
        
        # message for invalid input
        if p1_marker not in ['X', 'O']:
            print('Wrong input')
        
        # to allocate p2 marker
        else:
            acceptable_input.remove(p1_marker)
            p2_marker = acceptable_input[0]
            print('Player 1 will go first.')
        
    return p1_marker, p2_marker


# In[5]:


def game_continue(my_dict):
    
    answer = 'wrong'
    
    while answer.lower() not in ['yes', 'no']:
        
        answer = input('Are you ready to play? Enter Yes or No. ')
        
        if answer.lower() == 'no':
            return False


# In[6]:


def replacement_choice(p1_marker, p2_marker, position, game_round):
    
    if game_round % 2 != 0:
        my_dict[position] = p1_marker
        game_round += 1
    
    else:
        my_dict[position] = p2_marker
        game_round += 1
        
    return my_dict, game_round


# In[15]:


def game_win_check():
    
    win = False
    
    # List of all winning conditions
    if my_dict[1] == my_dict[2] == my_dict[3] and my_dict[1] != ' ':
        print('Yay you won!')
        win = True
        
    if my_dict[4] == my_dict[5] == my_dict[6] and my_dict[4] != ' ':
        print('Yay you won!')
        win = True
        
    if my_dict[7] == my_dict[8] == my_dict[9] and my_dict[7] != ' ':
        print('Yay you won!')
        win = True
    
    if my_dict[1] == my_dict[4] == my_dict[7] and my_dict[1] != ' ':
        print('Yay you won!')
        win = True
        
    if my_dict[2] == my_dict[5] == my_dict[8] and my_dict[2] != ' ':
        print('Yay you won!')
        win = True
        
    if my_dict[3] == my_dict[6] == my_dict[9] and my_dict[3] != ' ':
        print('Yay you won!')
        win = True
        
    if my_dict[1] == my_dict[5] == my_dict[9] and my_dict[1] != ' ':
        print('Yay you won!')
        win = True
        
    if my_dict[3] == my_dict[5] == my_dict[7] and my_dict[3] != ' ':
        print('Yay you won!')
        win = True
    
    # Draw condition
    if len(position_list) == 0 and win == False:
        print('Draw!')
        win = True
    
    return win


# In[8]:


def gameon_choice():
    
    choice = 'wrong'
    
    while choice.lower() not in ['yes','no']:
        
        choice = input('Would you like to play another round? Yes or No? ')
        
        if choice.lower() not in ['yes', 'no']:
            clear_output()
            print('Sorry, invalid input. Please choose Yes or No.')
            
    if choice.lower() == 'yes':
        return True
    else:
        return False


# In[16]:


# Variable to keep game playing

game_on = True

while game_on:
    
    # Tic Tac Toe Dictionary
    my_dict = { 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    # Varaible to prevent position override
    position_list = list(range(1,10))
    
    # Clear any historical values
    clear_output()
    p1_marker, p2_marker = game_start()
    clear_output()

    # Continue to game
    if game_continue(my_dict) == False:
        break
    
    else:
        display_game(my_dict)
    
    win = False
    game_round = 1
    
    while win == False:

        # Choosing position
        position = position_choice(game_round)
        clear_output()
        
        # Rewrite that position
        my_dict, game_round = replacement_choice(p1_marker, p2_marker, position, game_round)
                
        # Display current board
        clear_output()
        display_game(my_dict)
        
        # Check for win
        win = game_win_check()
        
    else:
        # Check if they want to continue playing
        game_on = gameon_choice()
        
else:
    clear_output()
    print('End of Game!')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




