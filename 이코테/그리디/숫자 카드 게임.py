"""
3 3
3 1 2
4 4 4 
2 2 2 
"""
    
n, m = map(int,input().split())
m_arr = []

for i in range(n):
    temp  = list(map(int,input().split()))
    m_arr.append(min(temp))
    
print(max(m_arr))