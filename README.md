# Fifa-Stat-Tracker

## About

This project is a culmination of the fact that I got sucked into Fifa Mobile over the summer (I know, ... it's quite the grim hobby). Unfortunately, the game doesn't keep track of the user's stats at all, so I decided to make this for myself. I found that it helped me identify offensive patterns that are more effective for me, and now I'm able to beat the World Cup campaign consistently with worse and worse teams :).

## Requirements

The only libraries that I used are Django 4.2.3 as well as django-crispy-forms 2.0. To run the app, cd into the fifa-stat-tracker folder which contains `manage.py` and run the following command: `python manage.py runserver`

## Demo
Create a team and add players to it using the Make Team Page:

![Create Team](/demo/CreateTeamGif.gif)

Start a game and keep track of stats for the game using the Start Game Page:

![Play Game](/demo/PlayGameGif.gif)

View player stats as well as team stats for each team created:

![View Team Stats](/demo/ViewTeamStatsGif.gif)

Use the Top Players and User Stats pages to see the top performing players as well as other useful stats:

![View User Stats](/demo/ViewUserStatsGif.gif)
