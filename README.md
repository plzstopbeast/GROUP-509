How To Play Game -
1. Run program - Going on Terminal - Typing - python3 uno2.py
2. Select number of players to play up to 4
3. Enter 1 or Single Round or 2 For Endless
4. Top Card is the card that is need to match either color or number
5. Shows Players Hand(Cards that player has) 
6. Has a arrow near card that can be used
7. Special Cards(Wild, Draw Four, Reverse, Draw Two, Skip)
Wild - Select Any Color (Blue, Yellow, Green, Red), Draw Four - Next Player Draws Four, Reverse - Goes Back
To player prior, Draw Two - Next Player Draws Two, Skip - Skips next players turn
8. Winner is determined to player who doesn't have anymore card.


Annotated Bibliography -
GeeksforGeeks. “Enumerate() in Python.” GeeksforGeeks, 20 Jan. 2025, www.geeksforgeeks.org/enumerate-in-python.
 - Explains and how to use the enumerate() function properly.

W3Schools.com. www.w3schools.com/python/ref_list_extend.asp.
- Explains the functionality of the .extend() method.

Attributions
Method/Function |     Author     | Techniques Demonstrated
Card.__repr__   , Mezzaiah Cooper , Magic Method (repr) for string representation
Card.matches    , Muntasir Rahman , Conditional Expression
Deck.__init__   , Dana Balbuena   , Comprehension Expression
Player.draw_card, Mezzaiah Cooper , Optional Parameter - drawing number of cards
Player.play_card, Mezzaiah Cooper   , F String for displaying cards
UnoGame , Samuel Adu , Composition of two custom classes
UnoGame.play_turn, Samuel Adu, Handling user input for game progression