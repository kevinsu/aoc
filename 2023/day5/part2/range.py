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

  def get_overlap(self, start, range_length):
    # No overlap
    if start + range_length < self.source_range_start:
      return None, None 
    if self.source_range_start + self.range_length < start:
      return None, None 
    if start < self.source_range_start:
      start_overlap = self.source_range_start
      if start + range_length < self.source_range_start + self.range_length:
        end_overlap = start + range_length
        end = self.source_range_start + self.range_length
        return [(self.source_range_start, end_overlap - start_overlap), (self.destination_range_start, end_overlap - start_overlap)]  
      else:
        end_overlap = self.source_range_start + self.range_length
        end = start + range_length
        return [(self.source_range_start, end_overlap - start_overlap), (self.destination_range_start, end_overlap - start_overlap)]  
    if start + range_length < self.source_range_start + self.range_length:
      return [(start, range_length), (self.destination_range_start+start-self.source_range_start, range_length)]
    start_overlap = start
    end_overlap = self.source_range_start + self.range_length
    end = start + range_length
    return [(start, end_overlap-start_overlap),(self.destination_range_start + start - self.source_range_start, end_overlap - start_overlap)] 
        
