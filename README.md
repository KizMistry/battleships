# Battleships
In this game, the user will attempt to destroy all of the computers battleships before the computer finds theirs.

[Battleships can be found here](https://battleship.herokuapp.com/)

![Screenshot](screenshot)
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
![intro](intro)

- Player and Computer boards generated
    - 5 Batteships are randomly generated for each board
    - Computers ships are hidden from the user
![board](board)
- User can input their desired attacking coordinates
- Outcome is returned after each attempt
![user_input](userinput)
![outcome](outcome)

- Input validation is performed after both user and computer attemps
    - Checks if the entered column is a single letter between A-E
    - Checks if the entered row is a single number between 1-5
    - Checks if no input was entered
    - Checks for duplicate guesses
    - Returns an error message if input is invalid
    - Can only progress if input is valid
![inputval](inputval)
- Play On option
    - User can choose to exit the game or play again
![playon](playon)

### Future features

- User will have the option to choose board size
- User will have the option to choose the number of ships
- The game will have a Best of 3 or 5 option
- Ships can be larger than 1 space
- User will have the option to place their own ships

## Data Model
-----

## Testing
-----
I have tested the Battleship game with the following tests:
| Test       | Expected           | Passed  |
| :------------- |:-------------:| :-----:|
| User clicks 'How To Play' button      | Modal opens | ✅ |
| User clicks 'x' button in the modal      | Modal closes | ✅ |
| User clicks outside modal area (while modal is open)| Modal closes | ✅ |
| User clicks 'Play' button before selecting hand     | An alert appears telling the user to select a hand      |   ✅ |
| User clicks any of the hand buttons | Border turns green and their hand displays in the users pick area       | ✅ |
| User clicks 'Play' button after selecting hand | Game runs, random hand generated and displayed,<br> correct results message displays and scores updated | ✅  |
| User clicks 'Reset' button | An alert appears and the scores, user pick, computer pick,<br> results message, and hand selections are reset to defualt | ✅  |
| Responsiveness of each screen size  | Each section and button adjusted size to fit all device displays |  ✅ |

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