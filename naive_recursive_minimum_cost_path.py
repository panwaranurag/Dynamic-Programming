#Python code for Minimum path cost path problem using Naive recursive implementation 


def minCost(cost,m,n):
    if m < 0 or n < 0:
        return "Please enter m and n as positive number"
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        n = cost[m][n] + min(minCost(cost, m-1, n-1),minCost(cost, m-1, n), minCost(cost, m, n-1))
        return n

if __name__ == "__main__":
    cost = [[1,2,3],[4,8,2],[1,5,3]]
    print "The minimum cost is", minCost(cost,2,2)    