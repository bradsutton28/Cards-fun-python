# In this Im going to be creating a baseline deck of playing cards in Python
# This will be the baseline so to speak that every game can build upon
import random
from tkinter import *
from PIL import ImageTk, Image


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def showCard(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for value in range(1,14):
                if (value == 1):
                    value = "Ace"
                if (value == 11):
                    value = "Jack"
                if (value == 12):
                    value = "Queen"
                if (value == 13):
                    value = "King"
                self.cards.append(Card(suit, value))

    def show(self):
        for c in self.cards:
            c.showCard()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def drawCard(self):
        # We want the bottom card since the deck is face down in card games
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.showCard()

    def fold(self):
        self.hand = []
        return self

    def drawX(self, deck, x):
        for i in range(x):
            self.hand.append(deck.drawCard())
        return self.hand


class Resize(Frame):

            # Defining the constructor in the class
            def __init__(self, master):
                # Calling constructor for method frame
                Frame.__init__(self, master)

                # Open and identify the image
                self.image = Image.open("card-table.PNG")

                # Create a copy of the image and store in variable
                self.img_copy = self.image.copy()

                # Define image using PhotoImage function
                self.background_image = ImageTk.PhotoImage(self.image)

                # Create and display the label with the image
                self.background = Label(self, image=self.
                                        background_image)
                self.background.pack(fill=BOTH,
                                     expand=YES)

                # Bind function resize_background to screen resize
                self.background.bind('<Configure>',
                                     self.resize_background)

            # Create a function to resize background image
            def resize_background(self, event):
                # Get the new width and height for image
                new_width = event.width
                new_height = event.height

                # Resize the image according to new dimensions
                self.image = self.img_copy.resize((new_width, new_height))

                # Define new image using PhotoImage function
                self.background_image = ImageTk.PhotoImage(self.image)

                # Change image in the label
                self.background.configure(image=self.background_image)


def main():
    deck = Deck()
    deck.shuffle()
    brad = Player("Brad")
    dealer = Player("Dealer")
    brad.drawX(deck, 2)
    brad.showHand()
    b = input("press 1 to continue to the dealer's drop or 2 to fold..\n")
    if b == '1':
        dealer.drawX(deck,5)
        print("---Dealer's Hand ---")
        dealer.showHand()
        print('---'+'\nYour Hand:')
        brad.showHand()
        table = Tk()
        table.title("Card Table")
        table.geometry("500x500")
        # Call the class components
        # and display it on table
        resizeTable = Resize(table)
        resizeTable.pack(fill=BOTH, expand=YES)
        resizeTable.mainloop()


main()


