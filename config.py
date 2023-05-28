
from random import randint, choice

#-----Data Set Function for Assessing Your Solution------------------#
#
# The function in this module generates the data sets that will be
# used to assess your solution.
#
# Do NOT change any of the code in this module.  Do NOT submit a copy
# of this module with your solution - we will use our own copy to
# assess your code.
#
# The following function creates a random data set defining the
# overall image to draw.  Your program must work for ANY data set that
# can be produced by this function.  The results returned by calling
# this function will be used as the argument to your data visualisation
# function during marking.  For convenience during code development
# and marking this function also prints the data set generated to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
def symbol_actions(width = 1, height = 1):

    # Define the ways the entities can move around the grid
    directions = ['East', 'West', 'North', 'South']
    
    # Choose the total number of entity actions
    num_actions = randint(0, 20)

    # Create the data set
    actions_list = []

    # Create the individual steps
    for step in range(0, num_actions):
        # Choose which way the entity wants to move
        direction = choice(directions)

        # Choose the number of cells the entity wants to move
        # (ignoring the limitations on their ability to do so)
        if direction in ['North', 'South']:
            num_cells = randint(1, height // 3)
        else:
            num_cells = randint(1, width // 2)
        # Add the chosen action to the data set
        actions_list.append([num_cells, direction])

    # Print the whole data set to the shell window, laid out
    # so that it's easy to distinguish the actions attempted by
    # the entity
    print('The entity actions to visualise are as follows:\n')
    print(str(actions_list).replace(', [', ', \n ['))
    # Return the data set to the caller
    return actions_list

#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
# Some "fixed" data sets
#
# Developing code when the underlying data set changes randomly can
# be difficult.  To help you develop your code you can temporarily
# provide the call to the "actions" function defined in the
# assignment template file with a "seed" value which will force it to
# produce a known data set.
#
# To do so, just put the seed value in the call to "actions" as
# its argument.  Of course, having completed your solution, your
# program must work for any list that can be returned by calling
# "actions" with no argument.
#
# Some examples of useful seeds follow.  Note that the following
# descriptions all assume that the grid has its default width and
# height (different behaviours will be created if the grid's size
# is changed). Seeds marked "+" were used in the client's briefing.
#
# The following seeds produce an empty actions list so the symbol
# is drawn at the starting dot, but no further moves are made
#
# +Seed 31 - perimeter count 1
# Seed 86 - perimeter count 1
#
# Each of the following seeds produces actions in which the character
#   DOES NOT attempt to leave the grid, and
#   processes all instructions
#
# +Seed 15 - completes all instructions, moves across to the RH perimeter
#           and back to the centre;
#           perimeter count 2
# Seed 19 - completes all instructions (only 1, to move east);
#           perimeter count 1
# Seed 20 - completes all instructions;
#           perimeter count 3
# Seed 43 - completes all instructions (only 1, to move north);
#           perimeter count 2
# Seed 49 - completes all instructions;
#           perimeter count 3
# Seed 68 - completes all instructions;
#           perimeter count 2

# Each of the following seeds produces actions in which the character
#   DOES attempt to escape from the grid, and
#   processes all instructions
#
# Seeds 3 - completes all instructions; attempts escape via west;
#           perimeter count 6
# +Seed 18 - completes all instructions; attempts escape via south;
#           perimeter count 4
# Seed 25 - completes all instructions; attempts escape via east and north;
#           perimeter count 6
# Seed 28 - completes all instructions; attempts to escape via west;
#           perimeter count 1
# Seed 29 - completes all instructions; attempts to escape via south and west;
#           perimeter count 7
# Seed 39 - completes all instructions; attempts to escape via west and north;
#           perimeter count 6
# Seed 45 - completes all instructions; attempts to escape via east;
#           perimeter count 7
#
# Each of the following seeds produces actions in which the character
#   DOES NOT attempt to escape from the grid, and
#   aborts because on perimeter too many times
#
# +Seed 80 - instructions aborted;
#           perimeter count 10
# Seed 98 - instructions aborted;
#           perimeter count 10
# Seed 112 - instructions aborted;
#           perimeter count 10
#
# Each of the following seeds produces actions in which the character
#   DOES attempt to escape from the grid, and
#   aborts because on perimeter too many times
#
# +Seed 36 - attempts escape via north; instructions aborted;
#           perimeter count 10
# Seed 27 - attempts escape via east and south; instructions aborted;
#           perimeter count 10
# +Seed 30 - attempts escape via west and east; instructions aborted;
#           perimeter count 10
# Seed 37 - attempts escape via east; instructions aborted
#           perimeter count 10

# Of course, you are free to choose other seed values to help you debug
# your code.
#
#--------------------------------------------------------------------#
