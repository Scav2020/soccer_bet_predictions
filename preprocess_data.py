# import the necessary packages

import pandas as pd
import numpy as np


# read in the raw csv data
understat_data = pd.read_csv('understat_data.csv')


# drop unnecessary columns
understat_data.drop(['xG','xGA','deep','ppda','ppda_allowed','matchesWithoutConceding'], axis=1, inplace=True)


# fill NaN values with 0
understat_data.fillna(0, inplace=True)


# map categorical variables to numerical
away_dict = {}
home_dict = {}
home_team = understat_data['h_team'].unique()
away_team = understat_data['a_team'].unique()

for i, team in enumerate(home_team):
    home_dict[team] = i
for i, team in enumerate(away_team):
    away_dict[team] = i

understat_data['h_team'] = understat_data['h_team'].map(home_dict)
understat_data['a_team'] = understat_data['a_team'].map(away_dict)


# engineering new features
understat_data['goal_diff'] = understat_data['h_goals'] - understat_data['a_goals']
understat_data['total_goals'] = understat_data['h_goals'] + understat_data['a_goals']
understat_data['goal_ratio'] = understat_data['h_goals'] / understat_data['a_goals']
understat_data['cs_diff'] = understat_data['h_clean_sheet'] - understat_data['a_clean_sheet']
understat_data['corner_diff'] = understat_data['h_corners'] - understat_data['a_corners']


# save cleaned data to a new csv file
understat_data.to_csv('cleaned_understat_data.csv', index=False, sep=',')
