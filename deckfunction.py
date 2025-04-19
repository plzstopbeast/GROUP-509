import random

COLORS = ['Red', 'Green', 'Blue', 'Yellow']
VALUES = [str(n) for n in range(0, 10)]  # Only number cards

def create_shuffled_deck():
    """
    Creates and returns a shuffled list of Card objects representing a standard UNO deck
    with only number cards. Also validates deck length after creation.
    
    Returns:
        list: A shuffled list of Card objects.
    
    Raises:
        Exception: If the final deck does not contain the expected number of cards.
    """
    class Card:
        def __init__(self, color, value):
            self.color = color
            self.value = value
        def __str__(self):
            return f"{self.color} {self.value}"

    # Create the deck (each number card appears twice per color)
    deck = [Card(color, value) for color in COLORS for value in VALUES * 2]

    # Shuffle the deck
    random.shuffle(deck)

    # Validate deck size: 4 colors × 10 numbers × 2 = 80 cards
    if len(deck) != 80:
        raise Exception(f"Deck size incorrect: expected 80, got {len(deck)}")

    return deck
