from main import hands, count_hands, Hand, score_hands, dealer_wins

for x in range(100):
    hand = hands()
    counted = count_hands(hand)
    score = score_hands(counted)
    hand = Hand(hand,counted,score)
    print("You - " + str(hand['player']['hand']))
    print("Dealer - " + str(hand['dealer']['hand']))
    if dealer_wins(hand):
        print("You lose to " + str(hand['dealer']['text']))
    else:
        print("You win with " + str(hand['player']['text']))
