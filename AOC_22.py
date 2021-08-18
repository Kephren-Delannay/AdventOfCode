player1_hand = [
    14,
    29,
    25,
    17,
    13,
    50,
    33,
    32,
    7,
    37,
    26,
    34,
    46,
    24,
    3,
    28,
    18,
    20,
    11,
    1,
    21,
    8,
    44,
    10,
    22
]
player2_hand = [
    5,
    38,
    27,
    15,
    45,
    40,
    43,
    30,
    35,
    9,
    48,
    12,
    16,
    47,
    42,
    4,
    2,
    31,
    41,
    39,
    23,
    19,
    36,
    49,
    6
]

def distribute_cards(player, cards):
    for c in cards:
        player.append(c)

def evaluate_cards():
    p1 = player1_hand.pop(0)
    p2 = player2_hand.pop(0)
    print("player 1 plays ", p1)
    print("player 2 plays ", p2)
    if p1 > p2:
        print("player 1 wins")
        distribute_cards(player1_hand, (p1, p2))
    else:
        print("player 2 wins")
        distribute_cards(player2_hand, (p2, p1))


def calculate_points(deck):
    score = 0
    for i in range(len(deck)):
        score += deck[i] * (len(deck) - i)
    return score

r=0
while len(player1_hand) > 0 and len(player2_hand) > 0:
    r+=1
    print("--------------round ", r, " -------------------------")
    evaluate_cards()
    print("p1 hand : ", player1_hand)
    print("p2 hand : ", player2_hand)

if len(player1_hand) == 0:
    print(calculate_points(player2_hand))
else:
    print(calculate_points(player1_hand))