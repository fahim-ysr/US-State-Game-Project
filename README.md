# US State Game Project

**In the "U.S. State Game" game the player has to guess the names of all 50 states in the United States. The game uses the turtle graphics library in Python to display a map of the United States, and the pandas library to read and manipulate data from a CSV file containing the names and coordinates of the states.**

**Preview below:**

<!DOCTYPE html>
<html lang="en">
  <body>
      <img src="demo.png" alt="US State Game Project" />
  </body>
</html>

**Tech Stack**

    The game is built using the following technologies:
    
        - Python: The programming language used for the game logic and user interface.
        
        - Turtle Graphics Library: A built-in Python library for creating graphics and visualizations.
        
        - Pandas: A powerful data manipulation and analysis library for Python.

**Code Breakdown**

    - Importing Modules
        The code starts by importing the necessary modules: turtle for graphics and pandas for data manipulation.

    - Display and Game Algorithms
        A turtle screen is created with the title "U.S. State Game".
        
        The image blank_states_img.gif is added as a shape to the turtle screen, which likely represents the map of the United States.
        
        The turtle shape is set to the added image.

    - CSV Algorithms
        The CSV file 50_states.csv is read using pandas, and the state names are stored in the all_states list.
        
        An empty list guessed_state is created to store the correctly guessed states.

    - Game Loop
        The game loop continues until the player has guessed all 50 states:

            The player is prompted to enter the name of a state using screen.textinput().
            If the entered state is valid (present in all_states) and not already guessed (not in guessed_state), the following actions are performed:

            A new turtle is created and hidden.
            
            The turtle moves to the coordinates of the guessed state (retrieved from the CSV data).
            
            The state name is written on the screen at the corresponding coordinates.
            
            The guessed state is added to the guessed_state list.
        
        - If the player enters "Exit", the game loop breaks, and a new CSV file missed_states.csv is created containing the list of states that the player did not guess.
