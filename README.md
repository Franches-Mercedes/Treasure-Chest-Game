# Treasure-Chest-Game

# Overview
This Python program creates a treasure chest game using a list of 15 random numbers ranging from 1 to 50 to represent treasure chest money. The list contains 16 items total, where index 0 is always set to 0 and indexes 1 through 15 represent the playable treasure chests.

One random chest is assigned a value of `-1`, which represents the losing chest. The user has 10 attempts to choose a valid chest number from 1 to 15.

If the selected chest contains a positive value, that amount is added to the user’s total cash. If the user selects the chest containing `-1`, the game ends immediately and the user loses. If the user successfully opens 10 chests without selecting the chest containing the  `-1`, they win and the program displays the total amount of money earned.

# Features
- Generates random treasure chest values
- Assigns one losing chest with a value of `-1`
- Accepts user input for chest selections
- Prevents invalid chest numbers
- Tracks total money earned
- Ends the game on a losing selection or after 10 successful attempts

# Language Used
- Python

# Skills Demonstrated
- Lists
- Loops
- Conditional statements
- Random number generation
- User input handling
- Accumulators

# How to Run
Run the program in Python from the command line or in an IDE of preference

