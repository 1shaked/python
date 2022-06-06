def findTheBestRoute(array):
    rows = len(array)
    cols = rows 

    # fix edge cases
    for row in range(rows):
        for col in range(row+1, cols):
            array[row][col] = 0
     

    bestRouteArr = array
    for row in range(1,rows):
        bestRouteArr[row][0] = bestRouteArr[row - 1][0] + bestRouteArr[row][0] 
        for col in range(1,row + 1):
            leftWay = bestRouteArr[row-1][col-1]
            straightWay = bestRouteArr[row-1][col]
            bestRouteArr[row][col] = max(leftWay, straightWay) + bestRouteArr[row][col]

    return max(bestRouteArr[rows - 1])



num = findTheBestRoute([
    [3, 0, 0 , 0],
    [7, 4, 0 , 0],
    [2, 4, 6 , 0],
    [8, 5, 9 , 3]
])
print(num)


num = findTheBestRoute([
    [8, 0, 0 , 0],
    [4, 4, 0 , 0],
    [2, 2, 6 , 0],
    [1, 1, 1 , 1]
])
print(num)