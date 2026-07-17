class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph={}
        for i in range(len(isConnected)):
            graph[i]=[]
        #print(graph)    
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    graph[i].append(j)
        # print(graph)
        visted=set()
        count=0
        for i in range(len(isConnected)):
            if i not in visted:
                count+=1
                q=deque()
                q.append(i)

                while q:
                    node=q.popleft()
                    visted.add(node)

                    for nei in graph[node]:
                        if nei not in visted:
                            q.append(nei)
        return count                           
