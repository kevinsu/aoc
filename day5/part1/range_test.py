import unittest

from range import Range

class TestRange(unittest.TestCase):
  def test_contains(self):
    range = Range(52, 50, 48)
    self.assertTrue(range.contains(66))
    self.assertFalse(range.contains(49))

  def test_get_destination_number(self):
    range1 = Range(52, 50, 48)
    range2 = Range(50, 98, 2)
    self.assertEqual(52, range1.get_destination_number(50))
    self.assertEqual(51, range2.get_destination_number(99))
    self.assertEqual(53, range1.get_destination_number(51))
    self.assertEqual(49, range2.get_destination_number(49))

if __name__ == '__main__':
  unittest.main()
