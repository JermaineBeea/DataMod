from Modules.GeneratePlayers import*
from Modules.DrawCard import*

for player in player_names:
  player_names[player] = drawCard()

print(player_names) 
