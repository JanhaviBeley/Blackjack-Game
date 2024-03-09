#Janhavi Beley 
#Blackjack Game 
#Introduction to Computer Science Course CS112

import random 
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.handValue = 0
        self.hand = []
    
    def __str__(self):
        report = "The final hand value of " + str(self.name) + " is " + str(self.handValue) +" with the hand of "+ str(self.hand)
        return report

    def update_hand_value(self, card, value):
        self.hand.append(card)

        if not card.startswith('Ace'):
            self.handValue += value
        elif self.handValue > 10:
            self.handValue += value 
        else: 
            self.handValue += 11

        return self.handValue
    
    def displayHand(self,name):
        print(name+"'s current hand of cards: "+str(self.hand))

class Card: 
    def __init__(self,rank,suit):
        self.num = rank
        self.suit = suit
        self.listOfCards = []
        
    def __str__(self):
        return str(self.listOfCards) 

    def create_deck(self):

        special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

        for suit in self.suit:
            for num in self.num:
                key = str(num) + ' ' + str(suit)

                if type(num) == int:
                    value = num
                else:
                    value = special_values[num]
            
                self.listOfCards.append([key, value])

        return self.listOfCards

def main():
    
    instructions()

    name1 = input("Player 1's name: ") 
    name2 = input("Player 2 or Dealer's name: ") 

    player = Player(name1)
    dealer = Player(name2)

    rank = [2,3,4,5,6,7,8,9,10,'Ace','King','Queen','Jack']
    suit = ['♠','♥','♣','♦']
    deck = Card(rank,suit)
    deck.create_deck()
    print()
    print("Here is your deck of card:",deck)
    print()
    
    count = 0
    while count < 4:
        #alternate players to receive the card
        if count % 2 == 0:
            temp_player = player
            temp_name = name1
        else: 
            temp_player = dealer
            temp_name = name2
        
        card, value = deal(deck.listOfCards)
        temp_player.update_hand_value(card, value)
        print(temp_name, "was dealt", card)

        count += 1

    player.displayHand(name1)
    dealer.displayHand(name2)

    print()
    print("Drawing cards time for player 1 "+name1)
    hitOrStay(player, name1, deck)
    time.sleep(1)
    print("Drawing cards time for player 2 or Dealer "+name2)
    dealerHitOrStay(dealer, name2, deck)

    time.sleep(3)
    print()
    print(player)
    print(dealer)

    resultReport(player,dealer,name1,name2) #Bust included in here

def instructions():

    print("Welcome to the Blackjack game!!!")
    time.sleep(3)
    print("In this game, each card in the deck has a value from 1 to 10. The player with the highest value sum of cards in their hand, still <= 21, wins (ties are allowed).")
    time.sleep(3)
    print("However, any player with a hand value > 21 loses (so both players might lose).")
    time.sleep(3)
    print("Here are the rules:")
    time.sleep(1)
    print("Two players will be assigned two random cards alternately. The second player will act as the dealer.")
    time.sleep(3)
    print("Player 1, after receiving the initial 2 cards, will decide whether to draw another card or hold their current cards. Type 'HIT' to draw and 'STAY' to hold.")
    time.sleep(3)
    print("Player 2, or the Dealer, will draw a new card if the hand value is <= 16 and hold otherwise. Type 'HIT' to draw and 'STAY' to hold.")
    time.sleep(3)
    print("The King, Queen, and Jack ranks are all assigned the value of 10.")
    time.sleep(3)
    print("If the current hand value is greater than 10, the Ace's value is 1; otherwise, it's 11.")
    time.sleep(3)
    print()

def deal(deck):

    random.shuffle(deck)
    card, value = deck.pop(0) #take the first card after each shuffle from the card to one player and remove it
    return(card,value)

def hitOrStay(player, name1, deck):

    turn = True
    while turn:
        choice = input(name1+", what will you choose? HIT or STAY: ") #choose to go or not

        if choice == "HIT":
            card, value = deal(deck.listOfCards)
            player.update_hand_value(card, value)
            print(name1, 'was dealt', card)
        elif choice == "STAY":
            print(name1+", your turn ends here with no more cards drawn.")
            turn = False #out of loop if choose stay
        
        player.displayHand(name1)

def dealerHitOrStay(dealer, name2, deck):

    while dealer.handValue <= 16:
        print(name2+", as your hand value is now under or equal to 16, you have to draw cards until the value is over 16 and the stop.")
        card, value = deal(deck.listOfCards)
        dealer.update_hand_value(card, value)
        print(name2,"was dealt", card)

    if dealer.handValue > 16:
        print(name2+", your hand value is now more than 16 so your turn ends here with no more card drawn.")
    
    dealer.displayHand(name2)

def resultReport(player,dealer,name1,name2):
    if player.handValue > 21 and dealer.handValue < 22:
        print("BUST!!!!",name1,"you lost the game!")
        print(name2,"is the winner of the game.")
    
    if dealer.handValue > 21 and player.handValue < 22:
        print("BUST!!!",name2,"you lost the game!")
        print(name1,"is the winner of the game.")
    
    if dealer.handValue > 21 and player.handValue > 21:
        print("BUST you all! Your hand values are over 21, so you both lost and we don't have a winner.")

    if player.handValue > dealer.handValue and player.handValue < 22:
        print(name1,"is the winner of this game.")
    elif player.handValue < dealer.handValue and dealer.handValue < 22:
        print(name2,"is the winner of the game.")
    elif player.handValue == dealer.handValue and dealer.handValue < 22:
        print("Seems that we have a tie.")

    print("The end! Good game players!")
main()