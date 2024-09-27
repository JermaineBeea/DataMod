Overview
This document explains the mathematical process for generating random, unique cards in a game using Unique IDs. The functionality is split across two files: RandGenerator.py and drawCard.py. These files work together to ensure random card selection and prevent any card from being drawn more than once using modular arithmetic and probabilities.

Key Concepts

1. Unique ID and Modular Arithmetic (`RandGenerator.py`)

In the card generation process, a Unique ID is assigned to each possible card, which is then used to select elements from different card categories (numbers, actions, wild cards, colors).

    Modular Arithmetic: The unique ID is processed through the function `modulos()`, which calculates indices for selecting specific elements from two sets (e.g., actions and colors).

    For a given unique_Id:
        indx_a and indx_b are calculated by dividing the unique_Id using modular arithmetic.

    This splits the ID into two parts, allowing for deterministic selection from multiple sets of card attributes.

    Product Map Size: The total number of possible unique card combinations is the sum of the sizes of the different card categories:
        Num_unique_cards = colourNum_size + actColour_size + wild_size

    This ensures that each unique ID corresponds to one possible card combination.
---

2. Drawing Random Cards (`drawCard.py`)

The function drawCard randomly selects a card based on its unique ID. There are three types of cards in the game:

    Number + Color (e.g., ['darkred', 5])
    Action + Color (e.g., ['act_1', 'darkblue'])
    Wild Cards (e.g., ['W_1', 'black'])

Each card type is selected based on the range of the unique ID, with different probabilities for each type depending on the size of their sets.

    Probabilities: Cards are drawn based on their category size:
        colourNum_size = len(colour_attr) * len(num_attribute)
        actColour_size = len(action_attr) * len(colour_attr)
        wild_size = len(wild_cards)

    A random unique_Id is generated, and based on its value, the card type is determined.

    Card Selection:
        If the unique_Id falls in the range for wild cards, a wild card is selected.
        If it falls within the range for action-color cards, the corresponding action and color are selected using modulos().
        Otherwise, a number-color card is selected using the same method.
---

3. Ensuring Uniqueness

To prevent duplicate cards, the function tracks drawn cards using the used_Id list. If the newly generated unique_Id has already been used, a new card is drawn.
---

4. Drawing Multiple Cards

The drawCards function allows multiple cards to be drawn in a single run. It repeatedly calls drawCard() while checking the used_Id list to ensure no duplicates. This ensures that each player receives a unique set of cards.
Example

    Total Cards:
    The total number of cards is calculated as:
        Num_unique_cards = 36 (number + color) + 12 (action + color) + 3 (wild cards) = 51

    Card Drawing: A random unique_Id is generated and checked against the used_Id list to ensure no duplicates. Based on the ID range:
        If the ID is within wild_size, a wild card is drawn.
        If it is within actColour_size, an action-color card is selected.
        Otherwise, a number-color card is drawn.

    Multiple Cards: The drawCards() function handles drawing multiple cards by repeatedly calling drawCard() and ensuring uniqueness.

Conclusion
The combination of modular arithmetic and probability-based selection provides a robust and fair system for drawing random cards while ensuring no duplicates. The unique ID system guarantees that each card is distinct, making this approach efficient and scalable for games involving multiple players and card types.