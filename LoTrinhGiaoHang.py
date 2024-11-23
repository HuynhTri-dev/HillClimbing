import random

matrix = [
    # A  B  C  D  E  F
    [0, 12, 9, 8, 0, 0],
    [12, 0, 0, 5, 1, 0],
    [9, 0, 0, 0, 0, 5],
    [8, 5, 0, 0, 0, 8],
    [0, 1, 0, 0, 0, 6],
    [0, 0, 5, 8, 6, 0]
]

def routeDistance(route, matrix):
    distance = 0
    for i in range(len(route) - 1): 
        if matrix[route[i]][route[i + 1]] == 0:
            distance += 999999
        distance += matrix[route[i]][route[i + 1]]
    distance += matrix[route[-1]][route[0]]  # Đảm bảo quay lại điểm đầu
    return distance

def getRoutes(currentRoute):
    newRoutes = []
    soDiem = len(currentRoute)
    for i in range(soDiem):
        for j in range(i + 1, soDiem):
            newRoute = currentRoute[:]
            newRoute[i], newRoute[j] = newRoute[j], newRoute[i]
            newRoutes.append(newRoute)  # Đã sửa dấu ngoặc vuông thành ngoặc tròn
    return newRoutes

def hillClimbing(matrix):
    soDiem = len(matrix)
    currentRoute = list(range(soDiem))
    random.shuffle(currentRoute)
    distanceCurrentRoute = routeDistance(currentRoute, matrix)
    
    while True: 
        newRoutes = getRoutes(currentRoute)
        bestRoute = None
        bestDistance = float('inf')

        for newRoute in newRoutes:
            distance = routeDistance(newRoute, matrix)
            if distance < bestDistance:
                bestRoute = newRoute
                bestDistance = distance

        if bestDistance >= distanceCurrentRoute:
            break
        
        currentRoute = bestRoute  # Đã sửa lại
        distanceCurrentRoute = bestDistance

    return currentRoute, distanceCurrentRoute

best_route, best_distance = hillClimbing(matrix)
print("Best route:", best_route)
print("Best distance:", best_distance)
