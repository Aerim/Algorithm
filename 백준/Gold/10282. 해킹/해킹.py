import heapq 

INF = 1e9

t = int(input())
ans = []

for i in range(t):

    n, d, c = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]

    for i in range(d):
        a, b, s = map(int,input().split())

        graph[b].append([a,s])

    distance[c] = 0
    que = []
    heapq.heappush(que,(0,c))

    while que:

        dist, node = heapq.heappop(que)

        if dist < distance[node]:
            continue

        for i in graph[node]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(que,(dist + i[1],i[0]))

    cnt = 0
    temp = 0
    # 마지막 컴퓨터가 바이러스 걸리는 시간 잘 생각
    for i in distance:
        if i != 1e9:
            cnt += 1

            if i > temp:
                temp = i

    ans.append([cnt,temp])

for i in ans:
    print(*i)