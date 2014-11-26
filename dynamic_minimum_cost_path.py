#Dynamic Programming implementation of MCP problem

def minCost(cost,m,n):
    tc = []
    
    for i in range(0,n+1):
        tc.append([])
        for j in range(0,m+1):
            tc[i].append(None)
            
    tc[0][0] = cost[0][0]
    
    #Initialize first column of total cost(tc) array
    for i in range(1,m+1):
        tc[i][0] = tc[i-1][0] + cost[i][0]
        
    #Initialize first row of tc array
    for j in range(1,n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]
        
    # Construct rest of the tc array
    for i in range(1,m+1):
        for j in range(1,n+1):
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]
    
    return tc[m][n]
    

if __name__ == "__main__":
    cost = [[1,2,3],[4,8,2],[1,5,3]]
    print "The minimum cost is", minCost(cost,2,2)    