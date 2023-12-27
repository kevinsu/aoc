import unittest
from part1 import *
from part2 import rmove, rrotate

class Test(unittest.TestCase):
  def test_swap_position(self):
    self.assertEqual('ebcda', swap('abcde', 'swap position 4 with position 0'))
    self.assertEqual('edcba', swap('ebcda', 'swap letter d with letter b'))

  def test_reverse(self):
    self.assertEqual('edcba', reverse('abcde', 'reverse positions 0 through 4'))
    self.assertEqual('adcbe', reverse('abcde', 'reverse positions 1 through 3'))

  def test_move(self):
    self.assertEqual('bdeac', move('bcdea', 'move position 1 to position 4')) 
    self.assertEqual('cdeba', move('bcdea', 'move position 0 to position 3')) 
    self.assertEqual('abdec', move('bdeac', 'move position 3 to position 0'))
    self.assertEqual('bcdea', move('bdeac', 'move position 4 to position 1'))

  def test_rmove(self):
    self.assertEqual('bcdea', rmove('bdeac', 'move position 1 to position 4')) 
    self.assertEqual('bcdea', rmove('cdeba', 'move position 0 to position 3')) 
    self.assertEqual('bdeac', rmove('abdec', 'move position 3 to position 0'))
    self.assertEqual('bdeac', rmove('bcdea', 'move position 4 to position 1'))

  def test_rotate(self):
    self.assertEqual('bcdea', rotate('abcde', 'rotate left 1 steps')) 
    self.assertEqual('ecabd', rotate('abdec', 'rotate based on position of letter b'))
    self.assertEqual('decab', rotate('ecabd', 'rotate based on position of letter d'))
    self.assertEqual('habcdefg', rotate('abcdefgh', 'rotate based on position of letter a'))
    self.assertEqual('ghabcdef', rotate('abcdefgh', 'rotate based on position of letter b'))
    self.assertEqual('fghabcde', rotate('abcdefgh', 'rotate based on position of letter c'))
    self.assertEqual('efghabcd', rotate('abcdefgh', 'rotate based on position of letter d'))
    self.assertEqual('cdefghab', rotate('abcdefgh', 'rotate based on position of letter e'))
    self.assertEqual('bcdefgha', rotate('abcdefgh', 'rotate based on position of letter f'))
    self.assertEqual('abcdefgh', rotate('abcdefgh', 'rotate based on position of letter g'))
    self.assertEqual('habcdefg', rotate('abcdefgh', 'rotate based on position of letter h'))

  def test_rrotate(self):
    self.assertEqual('abcde', rrotate('bcdea', 'rotate left 1 steps')) 
    self.assertEqual('abdec', rrotate('ecabd', 'rotate based on position of letter b'))
    self.assertEqual('ecabd', rrotate('decab', 'rotate based on position of letter d'))
    self.assertEqual('abcdefgh', rrotate('habcdefg', 'rotate based on position of letter a'))
    self.assertEqual('abcdefgh', rrotate('ghabcdef', 'rotate based on position of letter b'))
    self.assertEqual('abcdefgh', rrotate('fghabcde', 'rotate based on position of letter c'))
    self.assertEqual('abcdefgh', rrotate('efghabcd', 'rotate based on position of letter d'))
    self.assertEqual('abcdefgh', rrotate('cdefghab', 'rotate based on position of letter e'))
    self.assertEqual('abcdefgh', rrotate('bcdefgha', 'rotate based on position of letter f'))
    self.assertEqual('abcdefgh', rrotate('abcdefgh', 'rotate based on position of letter g'))
    self.assertEqual('abcdefgh', rrotate('habcdefg', 'rotate based on position of letter h'))
if __name__ == '__main__':
  unittest.main()
