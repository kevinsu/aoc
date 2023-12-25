import unittest
from part1 import Hailstone

class Test(unittest.TestCase):
  def test(self):
    h1 = Hailstone("219039780135044, 186558656984248, 267983068227965 @ 78, 54, 27")
    h2 = Hailstone("208221797969585, 86948144064012, 99756800446489 @ 106, 344, 344")
    self.assertEquals((244305633051517.16, 204050401311037.1), h1.get_intersection(h2)) 
    
if __name__ == '__main__':
  unittest.main()
