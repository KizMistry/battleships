# BattleShips
In this game, the user will attempt to destroy all of the computers battleships before the computer finds theirs.

[BattleShips can be found here](https://battleship.herokuapp.com/)

![BattleShips](/assets/images/battleships.png)
## How to play
-----
Upon starting the game, the users and computers board is generated 5 columns by 5 rows with 5 randomly placed ships.

The ships will display as `0` on their board whereas the computers ships will be hidden.

The user will attempt to correctly guess the coordinates of the computers ships by entering a column letter from A-E and a row number from 1-5.

The computer will have a random guess following the users attempt.

Successful attempts will update the opponents board replacing the ship `0`, with a hit marker displayed as `X`.

Unsuccessful attempts will display a miss as `-`.

The winner is the first to hit all opponents battleships.

## Features
-----
- Introduction message and game description.

![Welcome](/assets/images/welcome.png)

- Player and Computer boards generated
    - 5 Batteships are randomly generated for each board
    - Computers ships are hidden from the user

![Boards](/assets/images/boards.png)

- User can input their desired attacking coordinates

![User Inputs](/assets/images/user_input.png)

- Outcome is returned after each attempt

![Outcome](/assets/images/outcome.png)

- Input validation is performed after both user and computer attemps
    - Checks if the entered column is a single letter between A-E
    - Checks if the entered row is a single number between 1-5
    - Checks if no input was entered
    - Checks for duplicate guesses
    - Returns an error message if input is invalid
    - Can only progress if input is valid

![Input Validation](/assets/images/input_validation.png)

- Play On option
    - User can choose to exit the game or play again

![Play On](/assets/images/play_on.png)

### Future features

- User will have the option to choose board size
- User will have the option to choose the number of ships
- The game will have a Best of 3 or 5 option
- Ships can be larger than 1 space
- User will have the option to place their own ships

## Data Model
-----
To build this game I created 10 functions.

I first started with creating the 3 empty boards and setting the scores to zero before the main function is called.

When the main function is called it will run number of other functions in a specific order to enable the correct flow of the BattleShips game starting with the welcome function.

The welcome function will print a welcome message and rules before requesting a username to proceed.
Once returned, the username will be stored as the name variable and the next function will run.

The generate_ships function is then called for both the players board and the computers hidden board which will randomly place 5 ships on each board.

Next to be called is the update_board function which will print the boards.

The user_guess function is then called which will prompt the user for their first attempt after which will move onto the board_check function before moving onto the comp_guess function.

This process is repeated until the score limit is reached where the user will have the option to play again.


## Testing
-----
I have tested the Battleship game with the following tests:
| Test       | Expected           | Passed  |
| :------------- |:-------------:| :-----:|
| Enter a valid username      | Username printed to users board | ✅ |
| Enter without inputting username      | Error message requesting username and input field | ✅ |
| Enter username longer than 10 characters | Error message requesting username and input field | ✅ |
| Enter without inputting column letter or row number     | Error message requesting column/row and input field      |   ✅ |
| Enter a number into the column input | Error message requesting column and input field      | ✅ |
| Enter more than one letter/number | Error message requesting column and input field | ✅  |
| Enter letter/number that's not within the board | Error message requesting column and input field | ✅  |
| Enter coordinates previously entered  | Error message requesting column and input field |  ✅ |
| If all computer ships or user ships are hit  | Game finishes and an option to play again |  ✅ |
| Press 'Enter' to play again  | Game resets and runs again |  ✅ |
| Enter 'exit' to quit | Game ends with message and asks if certain |  ✅ |
| Enter 'y' for the 'Are you sure you want to quit' input| Exits the python program |  ✅ |
| Enter 'n' for the 'Are you sure you want to quit' input | Game resets and runs again |  ✅ |
| Enter nothing or invalid input for the 'Are you sure you want to quit' question | Error message requesting input is Y or N |  ✅ |

### Bugs

The BattleShips game works fully as expexcted without returning any errors or bugs

### Validator Testing

PEP8online.com and other online validators were not available at the time of creating this application.
All validation was done through the GitPod terminal and any problems were fixed using this method after revising the error messages.

There are 3 warnings, regarding the code, I'm aware of:
    - Redefining name 'user_score' from outer scope
    - Redefining name 'comp_score' from outer scope
    - Using the global statement

I have not yet found a way to reset the game boards and scores without the use of the global variables that doesn't include passing all variables through all functions and it becoming extremely messy and the code not running correctly.

Similar to the global variable problem, I have not found a way to update the scores using any other method.

## Deployment
-----
This project was deployed on Heroku using the following steps:

1. Select `Create new app`
2. Name the app, select region then click `Create app`
3. Within the Settings tab, in the Convig Vars section, create a Config Var called `PORT` and set this to `8000`
4. In the buildpacks section add `Python` and `NodeJS` in that order
5. Within the Deploy tab, select `GitHub` as the Deployment Method
6. Select `Connect to GitHub` and search for GitHub repositry name, select it, then click `Connect`
7. Click `Deploy`

The live link can be found here - https://battleship.herokuapp.com/

## Credits
-----
- Code Institute for the deployment terminal