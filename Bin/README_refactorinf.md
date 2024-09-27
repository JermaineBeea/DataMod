## Overview
This project has been refactored to organize the functionality across three main modules that are executed through the **MainRun.py** file. The objective was to split responsibilities and ensure clarity, modularity, and scalability in the program's structure. The program simulates a card game where players are generated, cards are drawn for each player, and players take turns.

### Key Modules:
1. **MainRun.py** - The main entry point that triggers the execution of the different game stages.
2. **GeneratePlayers.py** - Responsible for generating and validating player names.
3. **DrawCard.py** - Handles card drawing logic for the game.
4. **PlayerTurn.py** - Manages the player’s turn sequence and displays their cards.
---

## 1. MainRun.py
This is the entry point of the game. It triggers the key processes in order:

```python
from GeneratePlayers import RunGeneratePlayers
from DrawCard import RunDrawCards
from PlayerTurn import RunPlayerTurn

RunGeneratePlayers()  # Generate player names
RunDrawCards()        # Distribute cards to players
RunPlayerTurn()       # Handle player turns and display cards
```

### Workflow:
1. **RunGeneratePlayers**: Prompts the user for player names, validates the input, and handles any conflicts or invalid entries.
2. **RunDrawCards**: Draws a random set of cards for each player generated in the previous step.
3. **RunPlayerTurn**: Allows players to take their turn and displays their cards.
---

## 2. GeneratePlayers.py
This module focuses on:
- Validating player names using a flag system to detect invalid inputs.
- Handling name duplicates by suggesting modified names.
- Displaying a user interface (UI) for name input using **Tkinter**.

### Key Functions:
- **RunGeneratePlayers()**: Opens the UI where players can enter their names. It centers the widget on the screen and validates user input.
- **flagFilter()**: Checks if the entered name matches any invalid names or existing valid names using `difflib` to ensure no profane names are used.
- **checkDuplicate()**: Handles duplicate names by suggesting a modified name with random characters if needed.
- **parseInput()**: Validates and processes the input from the player, ensuring the input meets the required conditions.

The player data is stored in a global dictionary `players_generated` which will be passed to the card-drawing module.
---

## 3. DrawCard.py
This module handles:
- The card drawing logic, ensuring each player receives unique cards.
- There are different card types, including number cards, action cards, and wild cards, with specific attributes like colors.

### Key Functions:
- **drawCard()**: Draws a unique card for a player, ensuring no duplicates based on a generated ID.
- **drawCards()**: Draws multiple cards (7) for each player.
- **RunDrawCards()**: Loops through each player and distributes their cards by invoking `drawCards()`.

The `used_Id` list ensures that no card is drawn twice for any player.
---

## 4. PlayerTurn.py
This module is responsible for:
- Managing the turn order for players.
- Displaying each player’s cards when it’s their turn to play.

### Key Functions:
- **RunPlayerTurn()**: Displays a window with buttons for each player. Clicking the button will display the cards for that player.
- **sourceFunction()**: Displays the player's cards on the screen by calling `displayCards()` from the `Modules.DisplayCard`.
---

## Refactoring Highlights
- **Modularity**: The logic is now divided across three key modules, which enhances readability and maintenance.
- **Global Variables**: Used in a controlled manner for sharing data between modules, such as `players_generated` in `GeneratePlayers.py` and `players_cards` in `DrawCard.py`.
- **UI Integration**: The `Tkinter` library is used to build user-friendly interfaces for input, player turns, and card display.

This refactored structure allows for easier extensions, such as adding new game mechanics, refining UI components, or adjusting game rules.