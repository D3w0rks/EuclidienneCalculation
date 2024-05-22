import math


def euclideans(point1, point2):

    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def euclideanDistance(points):

    min_distance = float('inf')
    min_pair = None
    num_points = len(points)

    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = euclideans(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                min_pair = (points[i], points[j])

    return min_distance, min_pair


points = [
    (1, 2),
    (4, 5),
    (7, 8),
    (2, 1)
]

min_distance, min_pair = euclideanDistance(points)
print(f"The minimum Euclidean distance is {min_distance} between points {min_pair}")
