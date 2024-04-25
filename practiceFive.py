import math

def calculate_distance(point):
    return math.sqrt(point[0]**2 + point[1]**2)

def sort_points_by_distance_from_center(points):
    center = (0, 0)
    
    distances_and_points = [(calculate_distance(point), point) for point in points]
    
    sorted_points = sorted(distances_and_points, key=lambda x: x[0])
    
    return [point for distance, point in sorted_points]

points = [(3, 4), (1, 2), (-1, -1), (5, 5)]
sorted_points = sort_points_by_distance_from_center(points)
print("نقاط مرتب شده بر اساس فاصله از مرکز:", sorted_points)
