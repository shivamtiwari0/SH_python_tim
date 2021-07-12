import random
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def load_images(card_images):
    suits = ["spade", "club", "heart", "diamond"]
    face_cards = ["king", "queen", "jack"]
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for suit in suits:
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # Add it back to the pack
    deck.append(next_card)
    # Add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # Now return the card face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list.
    # Only one ace can have the value 11, and this will be reduce to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            card_value = 11
            ace = True
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score_label.set(dealer_score)
        dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")

    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")

    elif player_score < dealer_score:
        result_text.set("Dealer wins!")

    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")


def initial_deal():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    a = score_hand(dealer_hand)
    dealer_score_label.set(a)
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global player_hand
    global dealer_hand
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, bg='green')
    player_card_frame.grid(row=2, column=1, rowspan=2, sticky='ew')
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, bg='green')
    dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky='ew')

    result_text.set("")
    # Create list to store player and dealer hand
    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(bg='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, background='green', relief='sunken', bd=1)
card_frame.grid(row=1, column=0, columnspan=4, rowspan=2, sticky='ew')

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, bg='green', fg='white', text='Dealer').grid(row=0, column=0)
tkinter.Label(card_frame, bg='green', fg='white', textvariable=dealer_score_label).grid(row=1, column=0)

# embedded frame hold the card images.
dealer_card_frame = tkinter.Frame(card_frame, bg='green')
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky='ew')

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, bg='green', fg='white', text='Player').grid(row=2, column=0)
tkinter.Label(card_frame, bg='green', fg='white', textvariable=player_score_label).grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, bg='green')
player_card_frame.grid(row=2, column=1, rowspan=2, sticky='ew')

button_frame = tkinter.Frame(mainWindow, bg="green")
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Dealer', relief='raised', command=deal_dealer)
dealer_button.grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text='Player', relief='raised', command=deal_player)
player_button.grid(row=0, column=1)

game_button_frame = tkinter.Frame(mainWindow, bg='green')
game_button_frame.grid(row=4, column=0, columnspan=3, sticky='sw')
newGame = tkinter.Button(button_frame, text='New Game', relief='groove', command=new_game)
newGame.grid(row=0, column=2)


shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

# Load cards
cards = []
load_images(cards)
# Create a new deck of cards and shuffle them
deck = list(cards)
shuffle()
# Create list to store player and dealer hand
dealer_hand = []
player_hand = []


if __name__ == "__main__":
    play()
