import unittest

from part2 import *
class Test(unittest.TestCase):
  def test_can_go_north(self):
    distances = [[5, 4, 5], [4, 3, 4], [3, 2, 3], [2, 1, 2], [1, 0, 1]]
    all_shortest_paths=[[distances]]
    self.assertFalse(can_go_north(all_shortest_paths, 0, 0, 3))
    self.assertTrue(can_go_north(all_shortest_paths, 0, 0, 6))

  def test_can_go_south(self):
    distances = list(reversed([[5, 4, 5], [4, 3, 4], [3, 2, 3], [2, 1, 2], [1, 0, 1]]))
    all_shortest_paths=[[distances]]
    self.assertFalse(can_go_south(all_shortest_paths, 0, 0, 3))
    self.assertTrue(can_go_south(all_shortest_paths, 0, 0, 6))

  def test_can_go_east(self):
    distances = [[2, 3, 4, 5], [1, 2, 3, 4], [0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]
    all_shortest_paths=[[distances]]
    self.assertFalse(can_go_east(all_shortest_paths, 0, 0, 3))
    self.assertTrue(can_go_east(all_shortest_paths, 0, 0, 6))

  def test_can_go_west(self):
    distances = [[5, 4, 3, 2], [4, 3, 2, 1], [3, 2, 1, 0], [4, 3, 2, 1], [5, 4, 3, 2]]
    all_shortest_paths=[[distances]]
    self.assertFalse(can_go_west(all_shortest_paths, 0, 0, 2))
    self.assertTrue(can_go_west(all_shortest_paths, 0, 0, 6))

if __name__ == '__main__':
  unittest.main()
