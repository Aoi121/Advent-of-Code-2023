import sys

LETTERS_TO_POINTS = {
    'A':14,
    'K':13,
    'Q':12,
    'J':11,
    'T':10
}

def import_file():
    try:
        return open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File could not be opened.")
        quit()
    except IndexError:
        print("This program requires an input file to run.")
        quit()

# Parse the input + create a list of hands
# Convert each hand into its equivalent #
# of points. Add the deck + points into a
# dictionary. Sort the points.

# This is entirely wrong.
# It doesn't, and cannot, sort the hands
# with equal points.
# Could theorhetically convert the points
# back to hand form and sort them that was,
# or could just not convert to points, compile
# what cards are in each hand, and use
# some sorting alg to find the order.

def parse(lines):
    hands = []
    bid = []
    for line in lines:
        line = line[:-1]
        hands.append(line[:5])
        bid.append(line[6:])
    return [hands,bid]

def convert_to_points(hand):
    total_points = 0
    for i in range(0,len(hand)):
        card = hand[i]
        try:
            points = int(card)
        except ValueError:
            points = LETTERS_TO_POINTS[card]
        total_points += points
    return total_points

def main():
    input_file = import_file()
    lines = input_file.readlines()
    hands, bid = parse(lines)
    points = []
    points_and_bids = {}
    for i in range(0,len(hands)):
        hand_points = convert_to_points(hands[i])
        points.append(hand_points)
        points_and_bids[bid[i]] = hand_points
    points.sort()
    print(points)
    total = 0
    for i in range(0,len(bid)):
        b = bid[i]
        total += int(b) * int(points_and_bids[b])
        
if __name__ == "__main__":
    main()