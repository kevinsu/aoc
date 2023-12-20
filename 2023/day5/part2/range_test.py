import unittest

from range import Range

class TestRange(unittest.TestCase):
  def test_contains(self):
    range = Range(52, 50, 48)
    self.assertTrue(range.contains(66))
    self.assertFalse(range.contains(49))

  def test_get_destination_interval(self):
    range1 = Range(52, 50, 48)
    range2 = Range(50, 98, 2)
    self.assertEqual([(51, 46), (53, 46)], range1.get_overlap(51, 46))
    self.assertEqual([(98, 2), (50, 2)], range2.get_overlap(91, 10))
    self.assertEqual([(50, 35), (52, 35)], range1.get_overlap(10, 75))
    self.assertEqual([(75, 23), (77, 23)], range1.get_overlap(75,40 ))

if __name__ == '__main__':
  unittest.main()
