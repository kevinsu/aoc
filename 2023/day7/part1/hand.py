from enum import Enum

HandType = Enum('HandType', ['FIVE_OF_A_KIND', 'QUADS', 'FULL_HOUSE', 'SET', 'TWO_PAIR', 'PAIR', 'NADA'])

NUM_POSSIBLE_HANDS = 14**5

CARD_VALUES = {
  'A' : 14,
  'K' : 13,
  'Q' : 12,
  'J' : 11,
  'T' : 10
}

class Hand():
  def __init__(self, input_string):
    self.type, base_value = self.get_hand_type(input_string)
    tiebreaker = self.get_tiebreaker(input_string)
    self.value = base_value + tiebreaker
 
  def get_tiebreaker(self, input_string):
    multiplier = 1
    total = 0
    for c in reversed(input_string): 
      card_value = self.get_card_value(c)
      total += card_value * multiplier
      multiplier *= 14
    return total
 
  def get_card_value(self, card):
    if card in CARD_VALUES:
      return CARD_VALUES[card]
    return int(card)

  def get_hand_type(self, input_string):
    card_map = {}
    for c in input_string:
      if c not in card_map:
        card_map[c] = 0
      card_map[c] += 1
    if 5 in card_map.values():
      return HandType.FIVE_OF_A_KIND, NUM_POSSIBLE_HANDS * 6
    if 4 in card_map.values():
      return HandType.QUADS, NUM_POSSIBLE_HANDS * 5
    if 3 in card_map.values():
      if 2 in card_map.values():
        return HandType.FULL_HOUSE, NUM_POSSIBLE_HANDS * 4
      return HandType.SET, NUM_POSSIBLE_HANDS * 3
    if 2 in card_map.values():
      num_twos = sum(value == 2 for value in card_map.values())
      if num_twos == 2:
        return HandType.TWO_PAIR, NUM_POSSIBLE_HANDS * 2
      return HandType.PAIR, NUM_POSSIBLE_HANDS
    return HandType.NADA, 0
