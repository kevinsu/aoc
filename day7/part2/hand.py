from enum import Enum

HandType = Enum('HandType', ['FIVE_OF_A_KIND', 'QUADS', 'FULL_HOUSE', 'SET', 'TWO_PAIR', 'PAIR', 'NADA'])

NUM_POSSIBLE_HANDS = 14**5

HAND_VALUES = {
  HandType.FIVE_OF_A_KIND : NUM_POSSIBLE_HANDS * 6,
  HandType.QUADS : NUM_POSSIBLE_HANDS * 5,
  HandType.FULL_HOUSE : NUM_POSSIBLE_HANDS * 4,
  HandType.SET : NUM_POSSIBLE_HANDS * 3,
  HandType.TWO_PAIR : NUM_POSSIBLE_HANDS * 2,
  HandType.PAIR : NUM_POSSIBLE_HANDS,
  HandType.NADA : 0
}

CARD_VALUES = {
  'A' : 14,
  'K' : 13,
  'Q' : 12,
  'T' : 11,
  '9' : 10,
  '8' : 9,
  '7' : 8,
  '6' : 7,
  '5' : 6,
  '4' : 5,
  '3' : 4,
  '2' : 3,
  '1' : 2,
  'J' : 1,
}

class Hand():
  def __init__(self, input_string):
    self.type = self.get_hand_type(input_string)
    base_value = HAND_VALUES[self.type] 
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
    card_count = len(card_map)
    num_jokers = card_map.get('J', 0)
    if num_jokers >= 4:
      return HandType.FIVE_OF_A_KIND
    if num_jokers == 3:
      if card_count == 3:
        return HandType.QUADS
      if card_count == 2:
        return HandType.FIVE_OF_A_KIND
    if num_jokers == 2:
      if card_count == 4:
        return HandType.SET   
      if card_count == 3:
        return HandType.QUADS
      if card_count == 2:
        return HandType.FIVE_OF_A_KIND
    if num_jokers == 1:
      if card_count == 5:
        return HandType.PAIR
      if card_count == 4:
        return HandType.SET
      if card_count == 3:
        if 3 in card_map.values():
          return HandType.QUADS
        else:
          return HandType.FULL_HOUSE
      if card_count == 2:
        return HandType.FIVE_OF_A_KIND
    if 5 in card_map.values():
      return HandType.FIVE_OF_A_KIND
    if 4 in card_map.values():
      return HandType.QUADS
    if 3 in card_map.values():
      if 2 in card_map.values():
        return HandType.FULL_HOUSE
      return HandType.SET
    if 2 in card_map.values():
      num_twos = sum(value == 2 for value in card_map.values())
      if num_twos == 2:
        return HandType.TWO_PAIR
      return HandType.PAIR
    return HandType.NADA
