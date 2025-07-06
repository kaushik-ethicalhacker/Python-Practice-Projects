import random

def choose():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = []
    computer_cards = []

    
    for k in range(2):
        k = random.choice(cards)
        your_cards.append(k)
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")

    
    for c in range(2):
        c = random.choice(cards)
        computer_cards.append(c)
    print(f"Computer's first card: {computer_cards[0]}")

    
    sy = sum(your_cards)
    sc = sum(computer_cards)

    
    if sy == 21:
        return "You Win!"
    elif sc == 21:
        return "Computer won!"

    
    if sy > 21 and 11 in your_cards:
        position = your_cards.index(11)
        your_cards[position] = 1
        sy = sum(your_cards)

    if sc > 21 and 11 in computer_cards:
        position = computer_cards.index(11)
        computer_cards[position] = 1
        sc = sum(computer_cards)

    again = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if again == "y":
        new_card = random.choice(cards)
        your_cards.append(new_card)
        sy = sum(your_cards)
        if sy > 21 and 11 in your_cards:
            your_cards[your_cards.index(11)] = 1
            sy = sum(your_cards)
        print(f"Your cards: {your_cards}, current score: {sy}")

    else:
        while sc < 17:
            new_card = random.choice(cards)
            computer_cards.append(new_card)
            sc = sum(computer_cards)
            if sc > 21 and 11 in computer_cards:
                computer_cards[computer_cards.index(11)] = 1
                sc = sum(computer_cards)

    
    sy = sum(your_cards)
    sc = sum(computer_cards)

    print(f"Your final hand: {your_cards}, final score: {sy}")
    print(f"Computer's final hand: {computer_cards}, final score: {sc}")

    
    if sy > 21:
        return "You went over. Computer wins!"
    elif sc > 21:
        return "Computer went over. You win!"
    elif sy > sc:
        return "You win!"
    elif sy < sc:
        return "Computer wins!"
    else:
        return "It's a draw!"


def blackjack():
    asking = input("Do you want to play Blackjack? (y/n): ")
    if asking == "y":
        something = True
    else:
        something = False

    while something:
        logo = r"""
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """
        print(logo)
        print(choose())
        wanna_play_again = input("Do you want to play Blackjack? (y/n): ").lower()
        if wanna_play_again == "y":
            something = True
            print("\n" * 50)
        else:
            something = False

blackjack()
