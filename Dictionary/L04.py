"""Repeatedly ask the user to enter a team name and then how many games the team won and
how many they lost. Store this information in a dictionary where the keys are the team names
and the values are lists of the form [wins,losses].
(a) Using the dictionary created above, allow the user to enter a team name and print out
the team’s winning percentage.
(b) Using the dictionary, create a list whose entries are the number of wins of each team.
(c) Using the dictionary, create a list of all those teams that have winning records."""

teams = {
    "Lakers": [10, 5],
    "Heat": [8, 7],
    "Warriors": [12, 3],
    "Celtics": [9, 6],
    "Bulls": [7, 8],
    "Nets": [11, 4],
    "Suns": [13, 2],
    "Knicks": [6, 9],
    "Spurs": [5, 10],
    "Raptors": [8, 7]
}
x =len(teams)
name = input("team name: ").capitalize()
# for k,v in teams.items():
#     if name in teams.keys():
#         print('tem prsent',name)
#         wins = (v/x)*100
#     else:
#         pass
# print('winning percentage:', wins,'%')
if name in teams:
    wins, losses = teams[name]
    percentage = (wins / (wins + losses)) * 100
    print(f"Winning percentage: {percentage:.2f}%")
else:
    print("Team not found")
