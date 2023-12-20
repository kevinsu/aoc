import unittest

from range import Range
from seed_map import SeedMap

class TestSeedMap(unittest.TestCase):
  def test_build_seed_map(self):
    input = []
    input.append("seed-to-soil map:")
    input.append("50 98 2\n")
    input.append("52 50 48\n")

    seed_map = SeedMap(input)

    self.assertEqual('seed', seed_map.source)
    self.assertEqual('soil', seed_map.destination)
    self.assertEqual(52, seed_map.get_destination_number(50))
    self.assertEqual(51, seed_map.get_destination_number(99))
    self.assertEqual(53, seed_map.get_destination_number(51))
    self.assertEqual(49, seed_map.get_destination_number(49))
    self.assertEqual(101, seed_map.get_destination_number(101))
    self.assertEqual(1, seed_map.get_destination_number(1))

if __name__ == '__main__':
  unittest.main()
