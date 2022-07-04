n = int(input())

memory = []

for i in range(n+1):
    if i <= 1:
        memory.append(i)
    else:
        memory.append(memory[i-1] + memory[i-2])

print(memory[n])