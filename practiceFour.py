import math

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

point_a = (3, 4)
point_b = (6, 8)
distance = euclidean_distance(point_a, point_b)
print("فاصله اقلیدسی بین نقطه A و نقطه B:", distance)
