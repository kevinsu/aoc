def get_slope(line_segment):
	if line_segment[1] == line_segment[3]:
		return None
	return (line_segment[0]-line_segment[2]) / (line_segment[1] - line_segment[3])

def get_intercept(slope, x, y):
	return y - slope*x

def get_intersection(line_segment1, line_segment2):
	slope1 = get_slope(line_segment1)
	slope2 = get_slope(line_segment2)
	if slope1 == slope2:
		return None
	b1 = get_intercept(slope1, line_segment1[0], line_segment1[1])
	b2 = get_intercept(slope2, line_segment2[0], line_segment2[1])
	x = (b2-b1) / (slope1-slope2)
	y = slope1*x + b1
	min_x = min(line_segment1[0], line_segment1[2], line_segment2[0], line_segment2[2])
	max_x = max(line_segment1[0], line_segment1[2], line_segment2[0], line_segment2[2])
	min_y = min(line_segment1[1], line_segment1[3], line_segment2[1], line_segment2[3])
	max_y = max(line_segment1[1], line_segment1[3], line_segment2[1], line_segment2[3])
	if x > max_x or x < min_x or y > max_y or y < min_y:
		return None
	return x, y
	