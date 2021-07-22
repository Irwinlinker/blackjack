#Robert Marsh
#July 17, 2020
#Program runs a random hand of blackjack

##The program must utilize a tuple of SUITS and a tuple of PIPS.
##The program must utilize a nested sequence for a deck.
##A function create_deck() must be utilized to populate the nested sequence with all possible cards.
##A function create_hand() that selects and returns a random tuple from the nested sequence deck must 
##be created. It must also remove the cards from the deck
##A function sum_hand() must be used to total the pips on the two cards
##In the main portion of the program, call the create_deck() function
##Use a list to represent the player's hand with two cards.  You will pass this list to the sum_hand function
##Use a function sum_hand(hand) that will sum the cards in the hand and return a total.
##The function MUST accept a hand as a parameter and return the total
##If the sum is 21, tell the player that they won. Otherwise, print the total
##Print the deck



import random

def create_deck(deck): #function for making deck
    """creates the deck"""
    for pip in PIPS:
        for suit in SUITS:
            card = (pip, suit)
            deck.append(card)
            


def create_hand(hand): #function for maiking player hand
    """creates the players hand"""
    for i in range(2):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)




def sum_hand(hand): #function for adding up hand total
    """adds up the values of the cards"""
    total = 0
    for pip, suit in hand:
        if pip == "J" or pip == "Q" or pip == "K":
            total += 10
        elif pip == "A":
            total += 11
        else:
            total += int(pip)
    return total

def card_graphic(): #function for diplaying something that resembles a card
    """makes a rectangle that resembles a card"""
    card1 = hand[0][0] + hand[0][1]
    card1suit = hand[0][1]
    card2 = hand[1][0] + hand[1][1]
    card2suit = hand[1][1]
    printcards = f"""
----------------   ----------------        
| {card1}           |   | {card2}           |     
|              |   |              |
|              |   |              |
|              |   |              |
|      {card1suit}       |   |      {card2suit}       |
|              |   |              |
|              |   |              |
|              |   |              |
|              |   |              |
|           {card1} |   |           {card2} |  
----------------   ----------------
"""
    print(printcards)
    
    







#main program
car = [("person", "dog"), ("cat", "seat"), ("egg", "spoon")]
deck = [] #deck list
hand = [] #hand list
#suit unicode variables
HEART = "\u2665"
CLUB = "\u2663"
SPADE = "\u2660"
DIAMOND = "\u2666"
#pip and suit tuples
PIPS = ("2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A")
SUITS = (HEART, CLUB, SPADE, DIAMOND)
#call to functions
create_deck(deck)
create_hand(hand)
print(hand)
card_graphic()
total = sum_hand(hand)
#print total
print("\nYour total was", total)
if total == 21: #if total is 21
    print("Blackjack, you win!")
print()
#print remaining deck 
print(deck)

##for pip, suit, frisbee in car:
##    print("pip", pip)
##    print("suit", suit)
##    #print("frisbee", frisbee)
##for pip in car:
##    print("pip", pip[0], pip[1])
##    #print("suit", suit)
##    #print("frisbee", frisbee)
for pip, suit in car:
    print("pip", pip)
    print("suit", suit)
    #print("frisbee", frisbee)

input("\nPress Enter to exit.")
