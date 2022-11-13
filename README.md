## Battleships
-----
In this game, the user will attempt to destroy all of the computers battleships before the computer finds theirs.

[Battleships can be found here](https://battleship.herokuapp.com/)
## How to play
-----

## Features
-----
Welcome message, aim of game and legend.

User board and Computer board generated 5x5 with 5 randomly placed ships

user inputs there guesses

input validation to make sure input will accept
need 1 letter between A-E to progress
need 1 number between 1-5 to progress
coordinates can't be guessed twice

Future features

user can choose board size
user can choose number of ships
best of 3
ships larger than 1 space
user can place own ships

## Data Model
-----

## Testing
-----

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