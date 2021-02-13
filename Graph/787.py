# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# DFS
# Memo - (node, stops)
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        def dfs(node, stops, dst, n, graph, memo):
            
            if stops < 0:
                return float('inf')
            
            if node == dst:
                return 0                                    
                        
            if (node, stops) in memo:
                return memo[(node, stops)]
            
            ans = float('inf')
            for nei in range(n):
                if graph[node][nei] > 0:
                    ans = min(ans, dfs(nei, stops - 1, dst, n, graph, memo) + graph[node][nei])
                    
            memo[(node, stops)] = ans
            return ans
        
        graph = [[0 for _ in range(n)] for _ in range(n)]
        
        for u, v, p in flights:
            graph[u][v] = p
            
        res = dfs(src, K + 1, dst, n, graph, {})
        
        return res if res != float('inf') else -1
        
# Dijkstra Variant
# Stop tracking the min_dist so that it can traverse all path
from heapq import *
from collections import defaultdict

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        
        if not flights:
            return -1
        
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))
            
        hq = [(0, src, 0)]
        
        while hq:
            p, u, u_stops = heappop(hq)
            
            if u_stops > K + 1:
                continue
            
            if u == dst:
                return p
            
            for nei, nei_p in graph[u]:
                heappush(hq, (p + nei_p, nei, u_stops + 1))
            
        return -1
