# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Baseball GM/Home Team Win Predictor
---

## Problem Statement

As the new general manager of a small market baseball team that underperformed last season, I desparately want to improve the team's performance next year, but am limited by the following constraints: 

- I have less resources than larger market teams

- And thus, most likely will not get the high-impact stars players

Because of these contraints, my strategy is to identify lesser-known or "under the radar" players who are above average in one or two key areas for possible addition to the team.

Before I make any moves, I need to answer two questions:

- What are the elements that most contribute to a team's winning? 

- Which players should I add to improve the team?

In addition to improving the team's on-field performance, I want to enhance the fan experience by easing traffic congestion after the game and increasing fan engagement through a new app, "Will the Home Team Win?" that helps them decide whether to stay or leave early and beat the traffic, based on the likelihood of the home team winning that particular game.

## Definition of Success

I define success was identifying lesser known/"under the radar" players to possibly add to the team, and prototype app that predicts whether the home team will win with an accuracy rate of at least 60%.

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

* [Lahman Baseball Database](https://www.seanlahman.com/baseball-archive/statistics/): A database of open-source baseball statistics created and maintained by investigative reporter, Sean Lahman. This database contains pitching, hitting, and fielding statistics for Major League Baseball from 1871 through 2021.  It includes data from the two current leagues (American and National), the four other "major" leagues (American Association, Union Association, Players League, and Federal League), and the National Association of 1871-1875. You can find more information about Sean on his [website](https://www.seanlahman.com/). [Data Dictionary](https://www.seanlahman.com/files/database/readme2021.txt)

* [Retrosheet Game Logs](https://www.retrosheet.org/gamelogs/index.html): The game logs contain a record of major league games played from 1871-2020. At a minimum, it provides a listing of the date and score of each game. The logs include information such as team statistics, winning and losing pitchers, linescores, attendance, starting pitchers, umpires and more. There are 161 fields in each record.  [Data Dictionary](https://www.retrosheet.org/gamelogs/glfields.txt) 
    - Please note the disclaimer related to Retrosheet data: The information used here was obtained free of charge from and is copyrighted by Retrosheet.  Interested parties may contact Retrosheet at www.retrosheet.org.


## Modeling/Prediction

I used data from the Retrosheet game logs of 146,691 baseball games after 1945 to train a logistic regression classification model to predict whether the home team will win or lose based on 14 predictor variables, 7 for the home team and 7 for the visiting team. These variables, which are the same for both teams, are number of:

- hits
- walks
- left on base
- caught stealing
- double plays
- errors
- batters hit-by-pitch

The model's accuracy rate is 95% which outperforms the null baseline accuracy of 53.8%. The model did not show signs of overfitting or underfitting since the accuracy rate for both the training and test sets was 95%. To see if I could improve the accuracy, I ran a grid search pipeline with different logistic regression hyperparameters, as well as a stacked model using random forest, gradient boost, and ada boost as level 1 estimators, and a logistic regression as the final estimator. None of these models outperformed the accuracy rate of 95% on the test set from the original logistic regression model. 

While the model's accuracy rate was 95% overall, it performed worse when it predicted the outcome of games whose margin of victory for either team was one-run. In other words, the model had a tougher time accurately predicting close games. The misclassification rate for games with a one-run margin of victory was 13%, while it was 2% for games with a two-run margin of victory, and 0% for games with a three run margin of victory. 

![This is an image](https://github.com/dw943893/baseball_predictor/blob/main/images/misclass_rate_by_game_marg_victory.png)


A possible reason for the model's higher misclassification rate for close games is the values of the predictor variables for both the home and visiting team are very similar in games where the scores are very close, making it harder to predict which team will win.

I do note that there is high multicollinearity between the predictor variables in the logistic regression model which makes the exponentialted logistic regression coefficients uninterpretable. However, since I am using this model for prediction not inference, multicollinearity is not an issue.
(because of multicollinearity between the predictor variables, the exponentiated coefficient values were not interpretable.)

## Findings/Recommendations


Looking at the 2021 season, there is generally a positive relationship between the number of wins and the number of above average players on the team. Intuitively, it makes sense to believe that the higher the number of above average players a team has, the more games the team will win. Examining the 2021 season, the data generally supports this claim, but not in every case.

![This is an image](https://github.com/dw943893/baseball_predictor/blob/main/images/team_num_ab_avgplayers_and_wins.png)

(point out Orioles and Giants; example of variation)
(language/graphic related to managers?)

How did I define an above average player? I considered a player above average if they were better than average in categories that most strongly correlated with team wins. What are these categories?

Analyzing the team statistics for seasons after 1945 (aka the Modern Era of baseball as defined by Major League Baseball), the offensive categories with the highest positive correlation (0.40 and above) with team wins are:

- runs scored
- hits 
- walks
- homeruns

![This is an image](https://github.com/dw943893/baseball_predictor/blob/main/images/features_corr_with_team_wins.png)


In other words, as a team's number of runs, hits, walks, or homeruns increase, so does their number of wins. The category that is most negatively correlated with winning (-0.40 and below) is Earned Run Average (ERA), which means as a team's ERA increases their number of wins decreases.


Based on these findings, I recommend adding the following lesser-known hitters who have been above average in runs batting in (RBI), hits, and walks in at least one season since 2017:

- Ryan McMahon (Rockies)
- Yoan Moncada (White Sox)
- Travis Shaw (Red Sox)

And adding the following lesser-known starting pitchers who have had better than average ERAs in at least one season since 2017:

- Cal Quantrill (Guardians)
- Logan Webb (Giants)
- Adrian Houser (Brewers)


caveat, I did not factor in important factors, such as injury

## Streamlit App

This app determines a team's chances of winning based on the home and visiting teams' offensive and defensive stats during the game. Consider the following scenario, which is anathema to hard-core fans, but might apply to casual fans:

- You're at a baseball game, which can get notoriously long. It's the fourth inning and the score is 0 - 0. You want to beat the traffic to make it to a dinner later that evening, but you don't want to leave and miss out on the fun if you think the home team win has a good chance of winning. What do you do? 

- Break out the "Will My Home Team Win?" app, enter the stats for each team up until that point, and out spits the probability that the home team will win. If the home team most likely will lose, you leave the game early to beat the traffic and make it to dinner on time!


## Potential Areas for Model Improvement

---

