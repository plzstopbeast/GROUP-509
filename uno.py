import random

COLORS = ['Red', 'Green', 'Blue', 'Yellow']
SPECIAL_CARDS = ["Skip", "Reverse", "Draw Two", "Wild", "Draw Four"]
VALUES = [str(n) for n in range(0, 10)] + SPECIAL_CARDS 

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        
    def matches(self, other):
        return self.color == other.color or self.value == other.value or self.value in ["Wild", "Draw Four"]
    def __repr__(self):
        return f"{self.color} {self.value}"

class Deck:
    def __init__(self):
        self.cards = [Card(color, value) for color in COLORS for value in VALUES if value not in ["Wild", "Draw Four"]]
        self.cards.extend([Card("Wild", "Wild") for _ in range(4)])
        self.cards.extend([Card("Wild", "Draw Four") for _ in range(4)])
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop() if self.cards else None
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw_card(self, deck, num = 1):
        for _ in range(num):
            self.hand.append(deck.draw())
    
    def play_card(self, top_card):
        print(f"\n{self.name}'s Hand: {self.hand}")
        valid_moves = [card for card in self.hand if card.matches(top_card)]
        
        if valid_moves:
            choice = int(input(f"Choose a card index (0-{len(valid_moves)-1}): "))
            return self.hand.pop(choice)
        print(f"{self.name} has no valid moves, drawing a new card.")
        self.draw_card(deck=1)
        return None 
    def __str__(self):
        return f"{self.name} ({len(self.hand)} cards)"