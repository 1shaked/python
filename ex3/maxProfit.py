def maxProfit(A: list[int]):
    start:int = 0
    end:int = 0
    profit:int = 0
    for index, val in enumerate(A):
        if val < A[end]:
            # calculate profit 
            profit += A[end] - A[start]
            start = index
            end = index
            continue
        elif val > A[end]:
            end = index

    profit += A[end] - A[start]        
    print(profit)

    return profit




def maxProfitOnlyTwo(A: list[int]):
    lenA = len(A)
    if lenA == 2:
        return [
            A[1]- A[0], # profit
            min(A),
            max(A)
        ]
    if lenA == 3:
        return [
            max(A[1]- A[0] , A[2]- A[1], A[2]- A[0]), # profit
            min(A),
            max(A)
        ]
    middle = int (lenA / 2)
    leftP, leftMinV, leftMaxV = maxProfitOnlyTwo(A[:middle:])
    rightP, rightMinV, rightMaxV = maxProfitOnlyTwo(A[middle::])
    return [
        max( rightMaxV - leftMinV, leftP, rightP ),
        min(leftMinV, rightMinV),
        max(leftMaxV, rightMaxV)
    ]
    

p = maxProfitOnlyTwo([7,10,7, 2 , 4, 8, 7])[0]

print(p)