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
    self.assertEqual([(1, 49), (52, 48), (50, 2), (100, 901)], seed_map.get_destination_intervals(1, 1000))
    self.assertEqual([(1, 49), (52, 26)], seed_map.get_destination_intervals(1, 75))
    self.assertEqual([(77, 23), (50, 2), (100, 975)], seed_map.get_destination_intervals(75, 1000))
    self.assertEqual([(77, 10)], seed_map.get_destination_intervals(75, 10))

if __name__ == '__main__':
  unittest.main()
