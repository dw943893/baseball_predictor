# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Improving Baseball Team Performance and Fan Engagement, a General Manager's Perspective
---

## Problem Statement

As the new general manager of a small market baseball team that underperformed last season, I desperately want to improve the team's performance next year, but am limited by the following constraints: 

- I have less resources than larger market teams

- And thus, most likely will not get the high-impact stars players

Because of these constraints, my strategy is to identify lesser-known or "under the radar" players who are above average in one or two key areas for possible addition to the team.

In addition to improving the team's on-field performance, I want to enhance the fan experience by easing traffic congestion after the game and increasing fan engagement through a new app, "Baseball Game Predictor" that helps them decide whether to stay for the entire game or leave early and beat the traffic, based on the likelihood of the home team winning that particular game.

Before I make any moves related to improving team performance, I need to answer two questions:

- What are the elements that most strongly correlate to team wins? 

- Which players should I add to improve the team?

## Definition of Success

I define success as identifying lesser known/"under the radar" players to possibly add to the team, and creating a prototype app that predicts whether the home team will win with an accuracy rate of at least 60%.

## Items in this Repo
1) Jupiter notebook files:

    - Data cleaning
           
        - "CAP_data_cleaning_compile.ipynb"
    
    - Exploratory Data Analysis:

        - "CAP_EDA.ipynb"

    - Model Tuning:
     
        - "CAP_Modeling.ipynb"

2) PDF file:

    - "baseball.pdf" presentation

3) Images folder:

    - .png files used in this readme

4) Streamlit folder:

    - Pickled logistic regression model:
    
        - logreg_home.pkl
    
    - Streamlit app file:
    
        - logreg_home_app.py



## The Data 

* [Lahman Baseball Database](https://www.seanlahman.com/baseball-archive/statistics/): A database of open-source baseball statistics created and maintained by investigative reporter, Sean Lahman. This database contains pitching, hitting, and fielding statistics for Major League Baseball from 1871 through 2021.  It includes data from the two current leagues (American and National), the four other "major" leagues (American Association, Union Association, Players League, and Federal League), and the National Association of 1871-1875. You can find more information about Sean on his [website](https://www.seanlahman.com/). [Data Dictionary](https://www.seanlahman.com/files/database/readme2021.txt)

* [Retrosheet Game Logs](https://www.retrosheet.org/gamelogs/index.html): The game logs contain a record of major league games played from 1871-2021. At a minimum, it provides a listing of the date and score of each game. The logs include information such as team statistics, winning and losing pitchers, linescores, attendance, starting pitchers, umpires and more. There are 161 fields in each record.  [Data Dictionary](https://www.retrosheet.org/gamelogs/glfields.txt) 
    - Please note the disclaimer related to Retrosheet data: The information used here was obtained free of charge from and is copyrighted by Retrosheet.  Interested parties may contact Retrosheet at www.retrosheet.org.

For the purposes of this analysis, we looked at team stats and game log data for seasons after 1945 (aka the Modern Era of Baseball as defined by Major League Baseball).

## Findings/Recommendations

What features are most strongly correlated with team wins?
Analyzing the post-1945 team stats for every baseball team up to and including the 2021 season, a duration that includes 1,780 teams, the offensive categories with the highest positive correlation (0.40 and above) with team wins are:

- runs scored (R)
- hits (H)
- walks (BB, bases on balls)
- homeruns (HR)

![This is an image](https://github.com/dw943893/baseball_predictor/blob/main/images/features_corr_with_team_wins.png)

In other words, as a team's number of runs, hits, walks, or homeruns increase, so does their number of wins. The category that is most negatively correlated with winning (-0.40 and below) is Earned Run Average (ERA), which means as a team's ERA increases, their number of wins decreases. This makes sense since ERA is the average number of runs a team gives up to the opponent. 

Intuitively, it makes sense to believe that the greater the number of players on a team who are better than average in these categories, the more wins that team will experience. To see if that rings true, I identified the players with above average numbers, and counted how many of these players were on each team. Looking at the 2021 season, there is a moderately positive relationship between the number of team wins and the number of above average players on the team. 

But this is not true in every case. Notice the Giants and the Orioles had the same number of above average players in the 2021 season, however, the Giants won over 100 games while the Orioles won 52 games, a wide variation in results. 

The dots with the team names are the teams that made the playoffs in the 2021 season. The Braves, highlighted in yellow, won the World Series by defeating the Astros.


![This is an image](https://github.com/dw943893/baseball_predictor/blob/main/images/team_num_ab_avgplayers_and_wins.png)




Based on these findings, I recommend adding the following lesser-known hitters whose average numbers in the aforementioned offensive categories (runs batted in (RBI), hits, walks, and homeruns) over the past five seasons have been better than the league average. I categorized a player as "lesser-known" based on my subjective domain knowledge as a MLB baseball fan.

- Ryan McMahon (Rockies) (Best season from 2017- 2021: 2021, RBI: 86, hits: 134, walks: 59, HR: 23)
- Yoan Moncada (White Sox) (Best season from 2017- 2021: 2019, RBI: 79, hits: 161, walks: 40, HR: 25)
- Travis Shaw (Red Sox) (Best season from 2017- 2021: 2017, RBI 101, hits: 147, walks: 60, HR: 31)

And adding the following lesser-known starting pitchers who's average ERA over the past five seasons have been better than the league average:

- Cal Quantrill (Guardians) (Best season from 2017- 2021: 2021, ERA: 2.89)
- Logan Webb (Giants) (Best season from 2017- 2021: 2021, ERA: 3.03 )
- Adrian Houser (Brewers) (Best season from 2017- 2021: 2021, ERA: 3.22)


There are risks with taking this approach. These players usually have a shorter track record of sustained above average performance, increasing the chances any potential deal will be a "bust" because the player does not perform as expected.

For reference, the average number of runs batting in, hits, walks, and homeruns for a player who played in 100 games one of more times within the past 5 seasons is 64 RBI, 100 hits, 46 walks, and 18 homeruns. The average ERA of starting pitchers who have started 20 games at least once in the past 5 seasons is 4.11 runs.



## Modeling/Prediction

Circling back to the goal of enhancing the fan experience through the "Baseball Game Predictor" app, I used data from the Retrosheet game logs of 146,691 baseball games from 1946 to 2021 to train a logistic regression classification model to predict whether the home team will win or lose based on 14 predictor variables, 7 for the home team and 7 for the visiting team. These variables, which are the same for both teams, are number of:

- hits
- walks
- left on base
- caught stealing
- double plays
- errors
- batters hit-by-pitch

The model's accuracy rate is 95% which outperforms the null baseline accuracy of 53.8%. The model was not underfit or overfit since the accuracy rate for both the training and test sets was 95%. In efforts to improve the accuracy, I ran a grid search pipeline with different logistic regression hyperparameters, as well as a stacked model using random forest, gradient boost, and ada boost as level 1 estimators, and a logistic regression as the final estimator. None of these models outperformed the accuracy rate of 95% on the test set from the original logistic regression model. 

While the model's accuracy rate was 95% overall, it performed worse when it predicted the outcome of games whose margin of victory for either team was one-run. In other words, the model had a tougher time accurately predicting close games. The misclassification rate for games with a one-run margin of victory was 13%, while it was 2% for games with a two-run margin of victory, and 0% for games with a three run margin of victory. 

![This is an image](https://github.com/dw943893/baseball_predictor/blob/main/images/misclass_rate_by_game_marg_victory.png)


A possible reason for the model's higher misclassification rate for close games is the values of the predictor variables for both the home and visiting team are very similar in games where the scores are very close, making it harder to predict which team will win.

I do note that there is high multicollinearity between the predictor variables in the logistic regression model which makes the exponentiated logistic regression coefficients uninterpretable. However, since I am using this model for prediction and not inference, multicollinearity is not an issue.


## Streamlit App

This app calculates a team's chances of winning based on the home and visiting teams' offensive and defensive stats during the game. Consider the following scenario, which is anathema to hard-core fans, but might apply to casual fans:

- You're at a baseball game, which can get notoriously long. It's the fourth inning and the score is 0 - 0. You want to beat the traffic to make it to a dinner later that evening, but you don't want to leave and miss out on the fun if you think the home team has a good chance of winning. What do you do? 

- Break out the "Baseball Game Predictor" app, enter the stats for each team up until that point, and out spits the probability that the home team will win. If the home team most likely will lose, you leave the game early to beat the traffic and make it to dinner on time!

![This is an image](https://github.com/dw943893/baseball_predictor/blob/main/images/streamlit_app_screen_shot.png)


## Potential Areas for Model Improvement

Potentially improve the model's accuracy rate for predicting close games, where the margin of victory is one-run, by employing transfer learning from principal component analysis. 

---

