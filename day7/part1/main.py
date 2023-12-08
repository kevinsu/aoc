import sys
from hand import Hand

def main(argv):
  input_file = argv[0]
  file = open(input_file, 'r')
  hand_to_bid_map = {}
  hand_to_value_map = {}
  for line in file.readlines():
    hand_input, bid_input = line.split()
    hand = Hand(hand_input)
    hand_to_bid_map[hand_input] = int(bid_input) 
    hand_to_value_map[hand_input] = hand.value
  sorted_hands = sorted(hand_to_value_map.items(), key=lambda x:x[1])

  sum = 0 
  for rank, hand in enumerate(sorted_hands, 1):
    bid = hand_to_bid_map[hand[0]]
    sum += bid * rank
  print(sum) 

if __name__ == "__main__":
  main(sys.argv[1:])
