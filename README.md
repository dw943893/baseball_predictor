# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Baseball GM/Home Team Win Predictor
---

## Problem Statement

I am the new general manager of a small market baseball team that finished in last-place last season. I'm operating under the following constraints: 

- I have less resources than larger market teams

- And thus, most likely will not get the stars players who are above average in multiple categories that contribute to team wins

Because of these contraints, my strategy is to identify productive players that are lesser-known or "under the radar" who are above average in one or two key areas for possible addition to the team.

I desparately want to improve the team's performance but before I make any moves, I need to answer two questions:

- What are the elements that most contribute to a team's winning? 

- Which players should I add to improve the team?

I also want to ease the traffic congestion after the game and increase fan engagement by helping them decide whether to stay or leave based on the likelihood of the home team winning that particular game, through a new app "Will My Home Team Win?"


## Definition of Success

## Items in this Repo
1) Jupiter notebook files:

    - Data cleaning
           
        - "CAP_data_cleaning_compile.ipynb"
    
    - Exploratory Data Analysis:

        - "CAP_EDA.ipynb"

    - Model Tuning:
     
        - "CAP_Modeling.ipynb"

2) Streamlit folder:

    - Pickled logistic regression model:
    
        - logreg_home.pkl
    
    - Streamlit app file:
    
        - logreg_home_app.py


## The Data 

* [Lahman Baseball Database](https://www.seanlahman.com/baseball-archive/statistics/): A database of open-source baseball statistics created and maintained by investigative reporter, Sean Lahman. This database contains pitching, hitting, and fielding statistics for Major League Baseball from 1871 through 2021.  It includes data from the two current leagues (American and National), the four other "major" leagues (American Association, Union Association, Players League, and Federal League), and the National Association of 1871-1875. You can find more information about Sean on his [website](https://www.seanlahman.com/). The [Data Dictionary](https://www.seanlahman.com/files/database/readme2021.txt)

* [Retrosheet Game Logs](https://www.retrosheet.org/gamelogs/index.html): The game logs contain a record of major league games played from 1871-2020. At a minimum, it provides a listing of the date and score of each game. The logs include information such as team statistics, winning and losing pitchers, linescores, attendance, starting pitchers, umpires and more. There are 161 fields in each record.  [Data Dictionary](https://www.retrosheet.org/gamelogs/glfields.txt) 
    - Please note disclaimer related to Retrosheet data: The information used here was obtained free of charge from and is copyrighted by Retrosheet.  Interested parties may contact Retrosheet at www.retrosheet.org.

## Approach

Reviewing the baseball statistics of teams after 1945, the offensive categories with the highest positive correlation with a team winning are:

- runs scored
- walks
- hits
- home runs

The categories with the highest negative correlation with winning are Earned Run Average (ERA) and errors.

Based on this information, I sought to identify under the radar/lesser known players who are better than average in these categories to consider as additions to the team.


## Modeling/Prediction


## Findings/Recommendations

Conventional wisdom

Offense
Pitching
Defense
Coaching

Looking at the 2021 season, there is generally a positive relationship between the number of wins and the number of above average players on the team. Teams with more above average players on the roster have more wins, but that is not always the case.


## Streamlit App

This app helps fans determine your team's chances of winning based on the teams' offensive and defensive stats during the game.
Consider the following scenario, which is anathema to hard-core fans, but might apply to casual fans:

- You're at a baseball game, which can get notoriously long. It's the fourth inning and the score is 0 - 0. You want to beat the traffic to make it to a dinner later that evening, but you don't want to leave and miss out on the fun if you think the home team win has a good chance of winning. What do you do? 

- Break out the "Will My Home Team Win?" app, enter the stats for each team up until that point, and out spits the probability that the home team will win. If the home team most likely will lose, you leave the game early to beat the traffic and make it to dinner on time!


## Potential Areas for Model Improvement

---

