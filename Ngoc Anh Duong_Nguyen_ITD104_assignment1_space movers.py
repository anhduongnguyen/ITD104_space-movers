# -----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUTC's teaching unit
#  ITD104, "Building IT Systems", C1 2023.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
# put your student number here as an integer
student_number = 11479752
# put your name here as a character string
student_name = "Ngoc Anh Duong Nguyen"
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Task Description-----------------------------------------------#
#
#  SPACE MOVER
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "start_moving".  You are required to
#  complete this function so that when the program runs it draws a symbol
#  at various locations on a grid, using data stored in a list to
#  determine where to draw it.  See the various "client briefings"
#  in Canvas for full details.
#
#  You must use this template file to develop your program
#  and submit your final solution as a single Python 3 file only,
#  whether or not you complete all requirements for the assignment.
#
# --------------------------------------------------------------------#


# -----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.
# ***********DO NOT change any of the code in this section.***********
#

# Import standard Python modules needed to complete this assignment.
# You MUST not use any other modules for your solution.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless instructed.
# cell size in pixels (default is 100)
cell_size = 100
# number of cells across the width of grid (default is 8)
grid_width = 7  # was 8
# number of cells up the length of grid (default is 5)
grid_height = 7
# size of the margin left/right of the grid (pixels)
x_margin = cell_size * 2
# size of the margin below/above the grid (pixels)
y_margin = cell_size
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2.5
# font for the cell coords
small_font = ('Arial', cell_size // 5, 'normal')
# font for any other text
big_font = ('Arial', cell_size // 4, 'normal')

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 7, 'Grid must be at least 7 squares wide'
assert (grid_height >= 5) and (grid_height % 2 != 0), \
    'Grid must be at least 5 squares high and height must be odd'


#
# --------------------------------------------------------------------#


# -----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.
# ***********DO NOT change any of the code in this section.***********
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour='light grey',
                          line_colour='slate grey',
                          draw_grid=True,
                          label_spaces=True):  # NO! DON'T CHANGE THIS!

    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0)  # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)

        # Draw the vertical grid lines
        setheading(90)  # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3  # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2),
                 bottom_edge - y_offset)
            write(str(x_label + 1), align='right', font=small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 5, cell_size // 10  # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) +
                 (cell_size // 2) - y_offset)
            write(chr(y_label + ord("A")), align='center', font=small_font)

        # Mark the "special" cell
        goto(-cell_size * grid_width // 2 + 0.5 * cell_size, 0)
        dot(cell_size // 6)
        goto(cell_size * grid_width // 2 - 0.5 * cell_size, 0)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1) * cell_size) // 2, -(cell_size // 2))
        write('Draw your\nsymbol \nhere', align='right', font=big_font)
        # Right side
        goto(((grid_width + 1) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ncounter\nhere', align='left', font=big_font)

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor=True):
    tracer(True)  # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "start_moving" function.  ALL of your solution code
#  must appear in, or be called from, function "start_moving".  Do
#  NOT put any of your code in other parts of the program and do NOT
#  change any of the provided code except as allowed in the main
#  program below.
#

# All of your code goes in, or is called from, this function

# Hide the turtle
hideturtle()

# Determine the perimeter y coordinates
max_y_coords = [-350, 250]

# Determine the perimeter x coordinates
max_x_coords = [-350, 250]

# Determine the maximum perimeter count
perimeter_limit = 10

# Set a perimeter counter
perimeter_count = 0

# Set the coordinates where the counter number will be written
counter_coordinates = (440, -10)

# Set the coordinate where the ending message will be written
message_coordinates = (0, 360)

# Determine where the symbol will be drawn
symbol_coord = (-525, -40)

# Determine hello kitty's head radius for the function to draw
head_radius = 21.5

# Determine where the perimeter counter box will be drawn
perimeter_box_coords = (440, 10)

# Determine the coordinate for the perimeter counter caption
counter_caption_perimeter = (440, -70)
counter_caption_count = (435, -95)


# Check if the Hello Kitty is on the perimeter
def on_perimeter():
    global perimeter_count

    # Capture the x and y coordinates
    x_coordinate = round(xcor())
    y_coordinate = round(ycor())

    # Check if Hello Kitty is on the x or y perimeter coordinates
    if x_coordinate == max_x_coords[0] or x_coordinate == max_x_coords[1] or y_coordinate == max_y_coords[
        0] or y_coordinate == max_y_coords[1]:

        # Increment the perimeter counter
        perimeter_count += 1


# Update the perimeter counter number
def update_counter_box():
    # Check if the current perimeter count is less than 10
    if perimeter_count <= perimeter_limit:
        goto(perimeter_box_coords)
        shape("square")
        shapesize(5)
        color("black", "light pink")
        stamp()

        # Reset the turtle to it's default setting
        shape("classic")
        shapesize(1)

        # Write the current counter number
        goto(counter_coordinates)
        write(perimeter_count, font = ("arial", 40, "normal"), align = "center")

# Final message to be printed when instructions are completed
def finished_instructions_message():
        goto(message_coordinates)
        write("Hello Kitty has finished the journey!", font = ("arial", 40, "normal"), align = "center")

# Final message to be printed when instructions are aborted
def aborted_instructions_message():
        goto(message_coordinates)
        write("Oh no! Hello Kitty needs a nap", font = ("arial", 40, "normal"), align = "center")



# Draw Hello Kitty
def hello_kitty(head_radius):
    # Draw the 100 by 100 pixel square
    width(2)

    # Determine the square's background colour
    fillcolor("light pink")
    pd()
    begin_fill()

    # Determine the starting position of the drawing
    starting_x_position = xcor()
    starting_y_position = ycor()

    # Draw the box
    seth(0)
    forward(100)
    seth(90)
    forward(100)
    seth(180)
    forward(100)
    seth(270)
    forward(100)
    end_fill()
    pu()
    seth(90)
    forward(100)
    seth(0)
    forward(49.65)
    pu()

    # Draw hello kitty's head
    seth(270)
    forward(55)
    seth(180)
    forward(10)
    seth(0)
    pensize(1)
    pd()
    fillcolor("white")
    forward(head_radius)
    begin_fill()

    # Draw hello kitty's right cheek
    circle(head_radius, 130)
    end_fill()

    # Draw hello kitty's left cheek
    begin_fill()
    circle(head_radius, -130)
    backward(head_radius)
    circle(head_radius, -130)

    # Draw hello kitty's left ear
    left(90)
    circle(head_radius / 2, -90)
    right(45)
    circle(head_radius, -45)
    right(140)

    # Draw hello kitty's right ear
    forward(head_radius)
    right(140)
    circle(head_radius, -45)
    right(30)
    circle(head_radius / 2, -90)
    end_fill()
    pu()

    # Draw her bow
    seth(140)
    forward(head_radius / 1.18)
    pd()
    fillcolor("red")
    begin_fill()

    # Draw the left circle of bow
    circle(head_radius / 2.17)
    end_fill()
    pu()
    seth(269)
    forward(head_radius / 1.67)
    pd()
    begin_fill()

    # Draw the right circle of bow
    circle(head_radius / 2.17)
    end_fill()
    pu()
    seth(0)
    forward(head_radius / 2.22)
    seth(100)
    forward(head_radius / 4)
    pd()
    begin_fill()

    # Draw the small middle circle
    circle(head_radius / 4)
    end_fill()
    pu()

    # Draw her eyes
    pd()
    seth(-120)
    fillcolor("black")
    pu()
    pensize(1)
    forward(head_radius * 1.15)
    pd()
    begin_fill()

    # Draw her right eye
    circle(head_radius / 8)
    end_fill()
    seth(180)
    pu()
    forward(head_radius * 1.10)
    seth(270)
    pd()
    begin_fill()

    # Draw her left eye
    circle(head_radius / 8)
    end_fill()
    pu()

    # Draw her nose
    seth(0)
    forward(head_radius / 1.90)
    seth(270)

    # Go to the middle of the face
    forward(head_radius / 5.26)
    pd()
    fillcolor("yellow")
    begin_fill()
    circle(head_radius / 8.33)
    end_fill()
    pu()

    # Draw her top whiskers
    seth(10)
    forward(head_radius * 1.25)
    pd()
    forward(head_radius / 1.54)
    pu()
    backward(head_radius / 1.33)
    seth(180)
    forward(head_radius * 2.25)
    seth(170)
    pd()
    forward(head_radius / 1.54)

    # Draw her middle whiskers
    pu()
    seth(0)
    forward(head_radius * 3)
    seth(270)
    forward(head_radius / 2.72)
    seth(0)
    pd()
    forward(head_radius / 1.54)
    pu()
    seth(180)
    forward(head_radius * 3)
    pd()
    forward(head_radius / 1.54)

    # Draw her bottom whiskers
    pu()
    seth(0)
    forward(head_radius * 3)
    seth(270)
    forward(head_radius / 3.33)
    seth(350)
    pd()
    forward(head_radius / 1.54)
    pu()
    backward(head_radius / 1.33)
    seth(180)
    forward(head_radius * 2)
    seth(190)
    pd()
    forward(head_radius / 1.54)

    # Draw her dress
    pu()
    seth(0)
    forward(head_radius)
    seth(270)
    forward(head_radius / 4.26)
    pd()
    fillcolor("blue")
    begin_fill()
    seth(250)
    forward(head_radius * 1.5)
    seth(0)
    forward(head_radius * 2.25)
    seth(110)
    forward(head_radius * 1.5)
    end_fill()
    pu()

    # Draw her neckline
    seth(180)
    forward(head_radius)
    seth(270)
    fillcolor("yellow")
    begin_fill()
    pd()
    circle(head_radius / 2.5, 180)
    end_fill()
    pu()

    # Draw her right feet
    seth(180)
    forward(head_radius / 2.67)
    seth(270)
    forward(head_radius * 1.5)
    fillcolor("white")
    begin_fill()
    pd()
    forward(head_radius / 8)
    circle(head_radius / 2.85, 180)
    forward(head_radius / 5.71)
    end_fill()
    pu()

    # Draw her left feet
    pd()
    seth(180)
    forward(head_radius * 1.4)
    seth(270)
    fillcolor("white")
    begin_fill()
    forward(head_radius / 5.71)
    circle(head_radius / 2.85, 180)
    forward(head_radius / 5.71)
    end_fill()

    # Draw her left arm
    pu()
    seth(90)
    forward(head_radius * 1.5)
    seth(180)
    fillcolor("yellow")
    forward(head_radius / 1.54)
    seth(230)

    # Draw her sleeve
    pd()
    begin_fill()
    forward(head_radius)
    seth(330)
    forward(head_radius / 2.5)
    end_fill()
    pu()
    backward(head_radius / 2.5)
    seth(240)
    fillcolor("white")
    begin_fill()

    # Draw her hand
    pd()
    circle(head_radius / 3.33, 122.4)
    seth(70)
    forward(head_radius / 4)
    end_fill()
    pu()

    # Draw her right arm
    seth(90)
    forward(head_radius / 1.11)
    seth(0)
    forward(head_radius * 1.5)
    seth(315)
    fillcolor("yellow")
    begin_fill()
    pd()

    # Draw her sleeve
    forward(head_radius)
    seth(210)
    forward(head_radius / 2.22)
    end_fill()
    backward(head_radius / 2.22)
    seth(-240)
    fillcolor("white")
    begin_fill()
    pd()

    # Draw her hand
    circle(head_radius / 3.33, -123)
    seth(110)
    forward(head_radius / 4)
    end_fill()
    pu()
    goto(starting_x_position, starting_y_position)
    seth(0)

    # Check if the Hello Kitty is drawing on the perimeter
    on_perimeter()

    # Update the perimeter count box
    update_counter_box()

    # Return to previous position on the grid
    goto(starting_x_position, starting_y_position)

# Process all the moves on screen
def start_moving(data_set):
    pu()

    # Draw the symbol at the specified area
    goto(symbol_coord)
    hello_kitty(head_radius)

    # Write Hello Kitty caption under the symbol
    forward(50)
    seth(270)
    forward(30)
    write("Hello Kitty", font = ("arial", 20, "normal"), align = "center")

    # Write the caption for the perimeter counter box
    goto(counter_caption_perimeter)
    write("Perimeter", font = ("arial", 25, "normal"), align = 'center')

    goto(counter_caption_count)
    write("counter", font=("arial", 25, "normal"), align = "center")

    # Draw the symbol at square 1D
    square_1_D = (-350, -50)
    goto(square_1_D)
    hello_kitty(head_radius)

    # Go back to square 1D
    goto(square_1_D)


    # Move and draw Hello Kitty
    def draw_hello_kitty(steps, direction):

        # Determine the distance between each cell
        distance = 100

        # Loop through the steps
        for step in range(steps):

            # Check if the turtle can move in the given direction without going 
            # Out of bounds if so, move the turtle forward and draw a 
            # Hello Kitty image therwise, continue to the next step
            if direction == "North":
                if round(ycor()) + distance <= max_y_coords[1]:
                    seth(90)
                    forward(distance)
                    hello_kitty(head_radius)

            elif direction == "South":
                if round(ycor()) > max_x_coords[0]:
                    seth(270)
                    forward(distance)
                    hello_kitty(head_radius)

            elif direction == "East":
                if round(xcor()) + distance <= max_x_coords[1]:
                    seth(0)
                    forward(distance)
                    hello_kitty(head_radius)

            elif direction == "West":
                if round(xcor()) > max_y_coords[0]:
                    seth(180)
                    forward(distance)
                    hello_kitty(head_radius)

    # Loop through the list of instructions and draw accordingly
    for moving_instructions in data_set:

        # Check if the perimeter count has reached 10 already to abort
        if perimeter_count == perimeter_limit:

            #print the message for when instructions are aborted
            aborted_instructions_message()

            # Else, continue drawing Hello Kitty
            return
        draw_hello_kitty(moving_instructions[0], moving_instructions[1])

    # Print the final message if instructions are completed
    finished_instructions_message()


# --------------------------------------------------------------------#


# -----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.
# ***********DO NOT change any of the code in this section.***********
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's data generation function if available, but
### otherwise creating a dummy function that returns an empty
### list
if isfile('config.py'):
    print('\nData generation module available\n')
    from config import symbol_actions


    def actions(new_seed=None):
        seed(new_seed)
        return symbol_actions(grid_width, grid_height)
else:
    print('\nNo data generation module available!\n')


    def actions(dummy_parameter=None):
        return []

#
# --------------------------------------------------------------------#


# -----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas('light grey', 'slate grey', True, False)

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("Hello Kitty: Space Walker")

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "actions" function with a fixed seed for the
# ***** random number generator, but your final solution must
# ***** work with "actions()" as the argument to "start_travels",
# ***** i.e., for any data set that can be returned by
# ***** calling function "actions" with no seed.
start_moving(actions())  # <-- no argument for "actions" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible when the program
# ***** terminates as a debugging aid
release_drawing_canvas()

#
# --------------------------------------------------------------------#

