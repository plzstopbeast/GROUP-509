import random

COLORS = ['Red', 'Green', 'Blue', 'Yellow']
VALUES = [str(n) for n in range(0, 10)]  # Only number cards

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
    def matches(self, other):
        return self.color == other.color or self.value == other.value
    def most_common(cards):
        value_count = {}
        
    for card in cards:
        if card.value in value_count:
            value_count[card.value] += 1
        else:
            value_count[card.value] += 1
            
    most_frequent = max(value_count, key = value_count.get)
    
    return most_frequent

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw_card(self, deck):
        self.hand.append(deck.draw())
    
    def play_card(self, top_card):
        for i, card in enumerate(self.hand):
            if card.matches(top_card):
                return self.hand.pop(i)
        return None
    
    def has_won(self):
        return len(self.hand) == 0
    
    def __str__(self):
        return f"{self.name} ({len(self.hand)} cards)"
