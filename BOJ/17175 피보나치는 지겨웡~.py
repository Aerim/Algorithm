n = int(input())

memory = []

memory.append(1)
memory.append(1)

for i in range(2,n+1):
    memory.append(memory[i-1] + memory[i-2] + 1)

print(memory[-1] % 1000000007)