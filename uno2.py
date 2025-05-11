import random

COLORS = ['Red', 'Green', 'Blue', 'Yellow']
SPECIAL_CARDS = ["Skip", "Reverse", "Draw Two", "Wild", "Draw Four"]
VALUES = [str(n) for n in range(0, 10)] + SPECIAL_CARDS 

class Card:
    """Represents a single UNO card with a color and value.
    
    Technique Used:
    Magic Method: (__repr__) for string representation of the card.
    
    Attributes: 
        color (str): The color of card.
        value (str): The value of card.     
    
    Author: Muntasir Rahman
    """
    def __init__(self, color, value):
        """Initializes a card with a given color and value.
        
        Author: Muntasir Rahman
        """
        self.color = color
        self.value = value
        
    def matches(self, other):
        """Determines if card can be played based on the current top card
        
        Technique Used:
        -Conditional expression to check matching conditions.
        
        Args:
            other (Card): The current top card.

        Returns:
            bool: True if card can be played, False otherwise.
        
        Author: Muntasir Rahman
        """
        if self.value in ["Wild", "Draw Four"]:
            return True
        return self.color == other.color or self.value == other.value
    def __repr__(self):
        """Provides a string representation of card.
        
        Author: Mezzaiah Cooper
        """
        return f"{self.color} {self.value}"

class Deck:
    """Represents the deck of the UNO cards.
    
    Technique Used:
    - Comprehensions to generate the deck of cards.
    
    Attributes:
       cards (list): A shuffled deck of Card objects.
    
    Author: Dana Balbuena
    """
    def __init__(self):
        """Initializes the deck with a complete set of UNO cards.
        
        Author: Dana Balbuena
        """
        self.cards = [Card(color, value) for color in COLORS for value in VALUES if value not in ["Wild", "Draw Four"]]
        self.cards.extend([Card("Wild", "Wild") for _ in range(4)])
        self.cards.extend([Card("Wild", "Draw Four") for _ in range(4)])
        random.shuffle(self.cards)
    
    def draw(self):
        """Draws a card from the deck.

        Returns:
            Card or None: The top card of the deck, or None if the deck is empty.
            
        Author: Dana Balbuena
        """
        return self.cards.pop() if self.cards else None
    
class Player:
    """Represents a player in the UNO game.
    
    Technique Used:
    -Optional parameter (num) for drawing a variable number of cards.
    
    Attributes:
        name (str): The player's name
        hand (list): The player's hand of cards.
        
    Author: Mezzaiah Cooper
    """
    def __init__(self, name):
        """Initializes a player with a empty hand.
        Author: Mezzaiah Cooper
        """
        self.name = name
        self.hand = []
    
    def draw_card(self, deck, num = 1):
        """Draws a specified number of cards from the deck.

        Args:
            deck (Deck): The deck which to draw cards.
            num (int, optional): The number of cards to draw. Defaults to 1.
            
        Author: Mezzaiah Cooper
        """
        for _ in range(num):
            card = deck.draw()
            if card:
                self.hand.append(card)
    def play_card(self, top_card, deck):
        """Allows the player to play a valid card or draw one if none exist.
        
        Techniques Used:
        - a F-String containing expressions for displaying cards.

        Args:
            top_card (Card): The current top card in play.
            deck (Deck): The deck from which cards are drawn.

        Returns:
            Card or None: The played card or None if drawing.
        
        Author: Mezzaiah Cooper
        """
        print(f"\n{self.name}'s Turn: Top Card: {top_card}")
          
        valid_moves = [i for i, card in enumerate(self.hand) if card.matches(top_card)]
        
        if valid_moves:
            print("\nYour Hand:")
            for i, card in enumerate(self.hand):
                pointer = ">" if i in valid_moves else ""
                print(f"{pointer}{i}. {card}")
            
            while True:
                try:
                    choice = input("Choose card in Index or 'd' to draw: ").strip().lower()
                
                    if choice == 'd':
                        self.draw_card(deck)
                        print(f"{self.name} draws a card.")
                        return None
                
                    choice = int(choice)
                    if choice in valid_moves:
                        played_card = self.hand.pop(choice)
                        print(f"{self.name} plays {played_card}")
                        return played_card

                    print("Invalid choice. Card must match color/value or be Wild/Draw Four.")
                except(ValueError,IndexError):
                    print("Please enter a valid number or 'd' to draw.")
        else:
                print(f"{self.name} has no valid moves. Drawing new card.")
                self.draw_card(deck)
                return None
            
    def __str__(self):
        return f"{self.name} ({len(self.hand)} cards)"
class UnoGame:
    """Represents the UNO game session.
    
    Techniques Used:
    -Composition of two custom classes (Deck and Player)
    
    Attributes: 
         player_names (list): List of player names
         win_goal (int): Number of wins required to win game.
         scores (dict): Dictionary tracking player scores.
    
    Author: Samuel Adu
    """
    def __init__(self, player_names, win_goal=3):
        """Initializes an UNO game with given players and win goal.

        Author: Samuel Adu
        """
        self.player_names = player_names
        self.win_goal = win_goal
        self.scores = {name: 0 for name in player_names}

    def reset_game(self):
        self.deck = Deck()
        self.players = [Player(name) for name in self.player_names]
        
        self.turn_index = 0
        self.turn_direction = 1
        
        while True:
            self.top_card = self.deck.draw()
            if self.top_card.value not in ["Wild", "Draw Four"]:
                break  
        for player in self.players:
            player.draw_card(self.deck,5)

    def apply_special_effect(self, card):
        """Applies the special effects of a played card.
        
        Techniques Used:
        - Conditional expressions to modify gameplay mechanics
        
        Args:
            card (Card): The card played with special effects.
            
        Author: Samuel Adu
        """
        if card.value == "Skip":
            self.turn_index += self.turn_direction
        elif card.value == "Reverse":
            self.turn_direction *= -1
            self.turn_index += self.turn_direction
        elif card.value == "Draw Two":
            next_player = self.players[(self.turn_index + self.turn_direction) % len(self.players)]
            next_player.draw_card(self.deck, 2)
        elif card.value == "Draw Four":
            next_player = self.players[(self.turn_index + self.turn_direction) % len(self.players)]
            next_player.draw_card(self.deck, 4)
        elif card.value == "Wild":
           while True:
               new_color = input(f"{self.current_player().name}, choose a color (Red, Green, Blue, Yellow): ").capitalize()
               if new_color in COLORS:
                   card.color = new_color
                   print(f"Color changed to {new_color}!")
                   break
               print("Invalid color, try again.")
               
    def current_player(self):
        """Retrieves the current player based on the turn index.

        Returns:
            Player: The player whose turn it is.
            
        Author: Samuel Adu
        """
        return self.players[self.turn_index % len(self.players)]

    def play_turn(self):
        """Executes a single turn of the UNO game.
        
        Returns:
            bool: True if game should continue, False if a player has won a round.
        
        Author: Samuel Adu
        """
        current_player = self.current_player()
        print(f"\n{'-'*30}\nCurrent Scores: {self.scores}")
        print(f"\nTop Card: {self.top_card}")
        
        played_card = current_player.play_card(self.top_card,self.deck)

        if played_card:
            self.top_card = played_card
            self.apply_special_effect(played_card)

        if len(current_player.hand) == 0:
            print(f"\n{current_player.name} wins the round!")
            self.scores[current_player.name] += 1
            return False

        self.turn_index += self.turn_direction
        return True

    def play_one_round(self):
        """Plays a full round of UNO until a player wins the round.
        
        Techniques Used:
        -Handling user input for game progression.
        
        Author: Samuel Adu
        """
        self.reset_game()
        while self.play_turn():
            input("Press Enter to continue...")

    def show_scoreboard(self):
        """Displays the scoreboard with current win count for all players.
        
        Author: Mezzaiah Cooper
        """
        print("\nScoreboard:")
        for name, score in self.scores.items():
            print(f"{name}: {score} win{'s' if score != 1 else ''}")


    def check_for_game_winner(self):
        """Determines if a player has reached required number of wins.

        Returns:
            bool: True if a player has won a game, False otherwise.
            
        Author: Mezzaiah Cooper
        """
        for name, score in self.scores.items():
            if score >= self.win_goal:
                print(f"\n{name} wins the game with {score} wins. Game Over.")
                return True
        return False

    def start(self):
        """Starts the UNO game, allowing players to select 1 for single 2 for endless.
        
        Author: Samuel Adu
        """
        print("Welcome to Python UNO!")
        mode = input("Enter '1' for Single Round or '2' for Endless Mode: ").strip()

        if mode == "2":
            try:
                self.win_goal = int(input("Enter number of wins to win the game: "))
            except ValueError:
                print("Invalid input. Defaulting win goal to 3.")
                self.win_goal = 3

        round_num = 1
        while True:
            print(f"\nStarting Round {round_num}")
            self.play_one_round()
            self.show_scoreboard()
            print(f"Round {round_num} Over\n")

            if mode == "1" or self.check_for_game_winner():
                break

            again = input("Play another round? (y/n): ").strip().lower()
            if again != 'y':
                print("Thanks for playing!")
                break

            round_num += 1


# Start game
if __name__ == "__main__":
    num_players = int(input("How many players?(2-4): "))
    player_names = [f"Player {i+1}" for i in range(num_players)] 
    game = UnoGame(player_names)
    game.start()   