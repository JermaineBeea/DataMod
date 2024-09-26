from Modules.GeneratePlayers import*
from Modules.DrawCard import*

num_cards =  4
drawCards = lambda: [drawCard()[1] for _ in range(num_cards)]
for player in players_generated:
  players_generated[player] = drawCards()


