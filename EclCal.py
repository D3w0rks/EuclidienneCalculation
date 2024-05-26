import math

# 1. Noktaların Tanımlanması
points = [(1, 2), (3, 4), (6, 8), (7, 5)]

# 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 3. Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# 4. Minimum Mesafenin Bulunması
min_distance = min(distances)
print(f"Minimum Mesafe: {min_distance}")

# Mesafeleri ve minimum mesafeyi yazdırmak isterseniz:
for index, distance in enumerate(distances):
    print(f"Mesafe {index + 1}: {distance}")

print(f"Minimum Mesafe: {min_distance}")
