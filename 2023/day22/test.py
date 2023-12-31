import unittest
from part1 import Brick, Grid

class Test(unittest.TestCase):
  def test_2_pillar_support_all_disintegrates(self):
    brick1 = Brick('A', 1, 0, 1, 1, 0, 1)
    brick2 = Brick('B', 1, 1, 1, 1, 1, 1)
    brick3 = Brick('C', 0, 0, 5, 2, 2, 5)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    self.assertEqual(3, grid.get_count())

  def test_lower_pillar_drops_in_hole(self):
    brick1 = Brick('A', 0, 0, 1, 2, 0, 2)
    brick2 = Brick('B', 0, 2, 1, 2, 2, 2)
    brick3 = Brick('C', 2, 1, 1, 2, 1, 2)
    brick4 = Brick('D', 0, 1, 1, 0, 1, 2)
    brick5 = Brick('E', 1, 1, 2, 1, 1, 3)
    brick6 = Brick('F', 0, 0, 5, 2, 2, 10)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    grid.add_brick(brick6)
    self.assertEqual(6, grid.get_count())
    
  def test_same_pillar_drops_in_hole(self):
    brick1 = Brick('A', 0, 0, 1, 2, 0, 2)
    brick2 = Brick('B', 0, 2, 1, 2, 2, 2)
    brick3 = Brick('C', 2, 1, 1, 2, 1, 2)
    brick4 = Brick('D', 0, 1, 1, 0, 1, 2)
    brick5 = Brick('E', 1, 1, 3, 1, 1, 4)
    brick6 = Brick('F', 0, 0, 5, 2, 2, 10)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    grid.add_brick(brick6)
    self.assertEqual(6, grid.get_count())

  def test_higher_pillar_drops_in_hole(self):
    brick1 = Brick('A', 0, 0, 1, 2, 0, 2)
    brick2 = Brick('B', 0, 2, 1, 2, 2, 2)
    brick3 = Brick('C', 2, 1, 1, 2, 1, 2)
    brick4 = Brick('D', 0, 1, 1, 0, 1, 2)
    brick5 = Brick('E', 1, 1, 3, 1, 1, 5)
    brick6 = Brick('F', 0, 0, 5, 2, 2, 10)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    grid.add_brick(brick6)
    self.assertEqual(5, grid.get_count())

  def test_stacked_vertical_pillars(self):
    brick1 = Brick('A', 1, 1, 1, 1, 1, 2)
    brick2 = Brick('B', 1, 1, 5, 1, 1, 100)
    brick3 = Brick('C', 1, 1, 101, 1, 1, 102)
    brick4 = Brick('D', 1, 1, 104, 1, 1, 106)
    brick5 = Brick('E', 1, 1, 200, 1, 1, 300)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    self.assertEqual(1, grid.get_count())

  def test_stacked_vertical_squares(self):
    brick1 = Brick('A', 0, 0, 1, 1, 1, 2)
    brick2 = Brick('B', 1, 0, 5, 2, 1, 100)
    brick3 = Brick('C', 0, 1, 101, 1, 2, 102)
    brick4 = Brick('D', 1, 1, 104, 2, 2 , 106)
    brick5 = Brick('E', 0, 0, 200, 2, 2, 300)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    self.assertEqual(1, grid.get_count())

  def test_multiple_height_pillars(self):
    brick1 = Brick('A', 0, 0, 1, 0, 0, 5)
    brick2 = Brick('B', 1, 1, 2, 1, 1, 3)
    brick3 = Brick('C', 1, 1, 6, 1, 1, 8)
    brick4 = Brick('E', 0, 0, 200, 2, 2, 300)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    self.assertEqual(2, grid.get_count())
    
  def test_square_in_middle(self):
    brick1 = Brick('A', 0, 0, 1, 0, 0, 5)
    brick2 = Brick('B', 0, 0, 200, 2, 2, 300)
    brick3 = Brick('C', 1, 1, 302, 1, 1, 303)
    brick4 = Brick('D', 1, 1, 304, 1, 1, 306)
    brick5 = Brick('E', 0, 2, 500, 2, 2, 505)
    brick6 = Brick('F', 0, 0, 600, 2, 2, 700)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    grid.add_brick(brick6)
    self.assertEqual(3, grid.get_count())

  def test_spiral(self):
    brick1 = Brick('A', 0, 0, 1, 0, 0, 5)
    brick2 = Brick('B', 0, 0, 200, 2, 2, 300)
    brick3 = Brick('C', 2, 2, 201, 2, 0, 201) 
    brick4 = Brick('D', 2, 0, 202, 0, 0, 202) 
    brick5 = Brick('E', 0, 0, 203, 0, 2, 203) 
    brick6 = Brick('F', 0, 2, 204, 2, 2, 204) 
    brick7 = Brick('G', 1, 1, 205, 1, 1, 205)
    brick8 = Brick('H', 0, 0, 300, 2, 2, 400)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    grid.add_brick(brick6)
    grid.add_brick(brick7)
    grid.add_brick(brick8)
    self.assertEqual(2, grid.get_count())

  def test_spiral_same(self):
    brick1 = Brick('A', 0, 0, 1, 0, 0, 5)
    brick2 = Brick('B', 0, 0, 200, 2, 2, 300)
    brick3 = Brick('C', 2, 2, 201, 2, 0, 201) 
    brick4 = Brick('D', 2, 0, 202, 0, 0, 202) 
    brick5 = Brick('E', 0, 0, 203, 0, 2, 203) 
    brick6 = Brick('F', 0, 2, 204, 2, 2, 204) 
    brick7 = Brick('G', 1, 1, 205, 1, 1, 208)
    brick8 = Brick('H', 0, 0, 300, 2, 2, 400)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    grid.add_brick(brick6)
    grid.add_brick(brick7)
    grid.add_brick(brick8)
    self.assertEqual(2, grid.get_count())

  def test_spiral_higher(self):
    brick1 = Brick('A', 0, 0, 1, 0, 0, 5)
    brick2 = Brick('B', 0, 0, 200, 2, 2, 300)
    brick3 = Brick('C', 2, 2, 201, 2, 0, 201)
    brick4 = Brick('D', 2, 0, 202, 0, 0, 202)
    brick5 = Brick('E', 0, 0, 203, 0, 2, 203)
    brick6 = Brick('F', 0, 2, 204, 2, 2, 204)
    brick7 = Brick('G', 1, 1, 205, 1, 1, 300)
    brick8 = Brick('H', 0, 0, 300, 2, 2, 400)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    grid.add_brick(brick6)
    grid.add_brick(brick7)
    grid.add_brick(brick8)
    self.assertEqual(2, grid.get_count())

  def test_1(self):
    brick1 = Brick('A', 0, 0, 1, 0, 0, 1)
    brick2 = Brick('B', 0, 2, 1, 0, 2, 1)
    brick3 = Brick('C', 2, 0, 1, 2, 2, 2)
    brick4 = Brick('D', 0, 0, 3, 1, 1, 3)
    brick4 = Brick('E', 2, 0, 3, 2, 1, 3)
    brick5 = Brick('F', 0, 0, 4, 2, 1, 4)
    grid = Grid(3, 3)
    grid.add_brick(brick1)
    grid.add_brick(brick2)
    grid.add_brick(brick3)
    grid.add_brick(brick4)
    grid.add_brick(brick5)
    self.assertEqual(3, grid.get_count())
    
  def test_2(self):
    grid = Grid(3, 3)
    for i in range(0, 100):
      brick1 = Brick('A' + str(i), 0, 0, 1+500*i, 0, 0, 5+500*i)
      brick2 = Brick('B' + str(i), 0, 0, 200+500*i, 2, 2, 300+500*i)
      brick3 = Brick('C' + str(i), 2, 0, 201+500*i, 2, 2, 201+500*i)
      brick4 = Brick('D' + str(i), 0, 0, 202+500*i, 2, 0, 202+500*i)
      brick5 = Brick('E' + str(i), 0, 0, 203+500*i, 0, 2, 203+500*i)
      brick6 = Brick('F' + str(i), 0, 2, 204+500*i, 2, 2, 204+500*i)
      brick7 = Brick('G' + str(i), 1, 1, 205+500*i, 1, 1, 300+500*i)
      brick8 = Brick('H' + str(i), 0, 0, 300+500*i, 2, 2, 400+500*i) 
      grid.add_brick(brick1)
      grid.add_brick(brick2)
      grid.add_brick(brick3)
      grid.add_brick(brick4)
      grid.add_brick(brick5)
      grid.add_brick(brick6)
      grid.add_brick(brick7)
      grid.add_brick(brick8)
    self.assertEqual(101, grid.get_count())

if __name__ == '__main__':
  unittest.main()
