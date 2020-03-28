'''
A simple blackjack game
'''

import random
import os

suits = ['hearts', 'diamonds', 'clubs', 'spades']
numbers = list(range(2, 11)) + ['ace', 'jack', 'queen', 'king']

def createDeck():
    deck.clear()
    for suit in suits:
        for number in numbers:
            deck.append((suit, number))


def getValue(hand):
    sum = 0
    for card in hand:
        if type(card[1]) == int:
            sum += card[1]
        elif card[1] == 'ace':
            sum += 11
        else:
            sum += 10
    return sum

def hit():
    card = random.choice(deck)
    deck.remove(card)
    return card

def replay():
    valid = False
    while valid == False:
        again = input("Play again? (Y/N)")
        if again == 'Y' or again == 'y':
            os.system('cls')
            valid = True
            return True
        elif again == 'N' or again == 'n':
            os.system('cls')
            valid = True
            return False
        else:
            print("invalid input")

class User:
    def __init__(self, hand):
        self.hand = hand
        # self.bank = bank

    # def bet(self):
    #     self.bank -= bet

    # def win(self):
    #     self.bank += bet*2

    # def push(self):
    #     self.bank += bet
        
    def __len__(self):
        aceCount = 0
        total = getValue(self.hand)
        for card in self.hand:
            if card[1] == 'ace':
                aceCount += 1
        if getValue(self.hand) > 21:
            for x in range(aceCount):
                total -= 10
                if total < 21:
                    break
        return total

    def __str__(self):
        hand_string = ''
        for card in self.hand:
            hand_string += f" / {card[1]} of {card[0]}"
        return hand_string

class Bot:
    def __init__(self, hand):
        self.hand = hand

    def revealHand(self):
        hand_string = ''
        for card in self.hand:
            hand_string += f" / {card[1]} of {card[0]}"
        return hand_string

    def __len__(self):
        aceCount = 0
        total = getValue(self.hand)
        for card in self.hand:
            if card[1] == 'ace':
                aceCount += 1
        if getValue(self.hand) > 21:
            for x in range(aceCount):
                total -= 10
                if total < 21:
                    break
        return total

    def __str__(self):
        return f"{self.hand[0][1]} of {self.hand[0][0]}"

def checkInstantWin(target):
    if len(target) == 21:
        return True

#game loop

while True:
    deck = []
    createDeck()
    player = User([hit(), hit()])
    dealer = Bot([hit(), hit()])

    # while True:
    #     print(f"Your balance: {player.bank}")
    #     try:
    #         bet = int(input("Place your bet! "))
    #         if player.bank >= bet:
    #             player.bet()
    #             break
    #         print("Insufficient funds!")
    #     except:
    #         print("Please enter a number for your bet value!")

    print(f"The dealer has a {str(dealer)} and another hidden card")
    
    while True:
        print(f"In your hand is a {str(player)}")
        print(f"Your count: {len(player)}")

        minimised = False

        if checkInstantWin(player):
            print("lucky deal, you win! you were dealt 21!")
            # print(f"You have received ${bet*2}!")
            # player.win()
            break
        action = input("hit or stay?")

        if action == "hit":
            #hit the player
            new_card = hit()
            print(f"You are dealt a {new_card[1]} of {new_card[0]}")
            player.hand.append(new_card)
            #check if player hit 21
            if checkInstantWin(player):
                print("lucky deal, you win! you were dealt 21!")
                # print(f"You have received ${bet*2}!")
                # player.win()
                break
            #check if player busts
            if len(player) > 21:
                print(f"game over! you bust at {len(player)} with {str(player)}")
                # print(f"You have lost ${bet}!")
                break
        elif action == "stay":
            #Reveal dealer hidden card
            print(f"The dealers hidden card is a {dealer.hand[1][1]} of {dealer.hand[1][0]}")
            if checkInstantWin(dealer):
                print("unlucky deal, you lost! dealer dealt 21!")
                # print(f"You have lost ${bet}!")
                break
            #dealer keeps going until beats player or busts
            while len(dealer) < 21:
                #hit the dealer
                new_dealer_card = hit()
                print(f"Dealer is dealt a {new_dealer_card[1]} of {new_dealer_card[0]}")
                dealer.hand.append(new_dealer_card)
                #check if dealer hit 21
                if checkInstantWin(dealer):
                    print("unlucky deal, you lost! dealer dealt 21!")
                    # print(f"You have lost ${bet}!")
                    break
                #check if dealer busts
                if len(dealer) > 21:
                    print(f"you won! dealer bust at {len(dealer)} with {dealer.revealHand()}")
                    # print(f"You have received ${bet*2}!")
                    # player.win()
                    break
                #check if dealer wins
                elif len(dealer) > len(player):
                    print(f"you lost! dealer has higher total of {len(dealer)}!")
                    # print(f"You have lost ${bet}!")
                    break
            if len(dealer) == len(player):
                print(f"push! both scored 20!")
                # print(f"Your bet of {bet} has been returned!")
                # player.push()
            break
        else:
            print("invalid input")
    if not replay():
        break
        

