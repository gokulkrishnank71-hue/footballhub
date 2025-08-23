import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "data", "2000-25-data.csv")

df = pd.read_csv(csv_path)

# Replace these column names with the actual ones from your CSV
home_teams = df['HomeTeam'].unique()
away_teams = df['AwayTeam'].unique()

all_teams = sorted(set(home_teams) | set(away_teams))

print("All teams in dataset:")
for team in all_teams:
    print(team)
