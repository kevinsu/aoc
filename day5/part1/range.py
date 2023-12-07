class Range():
  def __init__(self, destination_range_start, source_range_start, range_length):
    self.destination_range_start = destination_range_start
    self.source_range_start = source_range_start
    self.range_length = range_length

  def contains(self, source_number):
    if source_number < self.source_range_start:
      return False
    if source_number > self.source_range_start + self.range_length:
      return False
    return True

  def get_destination_number(self, source_number):
    if not self.contains(source_number):
      return source_number
    return source_number - self.source_range_start + self.destination_range_start
