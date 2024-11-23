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
    distance += matrix[route[-1]][route[0]]  
    return distance

def getRoutes(currentRoute):
    newRoutes = []
    soDiem = len(currentRoute)
    for i in range(soDiem):
        for j in range(i + 1, soDiem):
            newRoute = currentRoute[:]
            newRoute[i], newRoute[j] = newRoute[j], newRoute[i]
            newRoutes.append(newRoute)  
    return newRoutes

def hillClimbing(matrix, maxRestarts=10):
    soDiem = len(matrix)
    bestOverallRoute = None
    bestOverallDistance = float('inf')

    for restart in range(maxRestarts):
        
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
            
            currentRoute = bestRoute
            distanceCurrentRoute = bestDistance

        
        if distanceCurrentRoute < bestOverallDistance:
            bestOverallRoute = currentRoute
            bestOverallDistance = distanceCurrentRoute
        
        print(f"i {restart + 1}: Lo trinh: {currentRoute}, Khoang cach: {distanceCurrentRoute}")

    return bestOverallRoute, bestOverallDistance

# Thực thi thuật toán
print("Cai tien voi bien the Random Restart Hill-Climbing")
bestRoute, bestDistance = hillClimbing(matrix, maxRestarts=10)
print("======================================")
print("Lộ trình tốt nhất toàn cục:", bestRoute)
print("Khoảng cách ngắn nhất toàn cục:", bestDistance)