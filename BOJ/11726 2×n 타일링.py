n = int(input())

memory = []

for i in range(n+1):
  if i == 0:
    memory.append(0)
  elif i == 1:
    memory.append(1)
  elif i == 2:
    memory.append(2)
  else:
    memory.append(memory[i-1] + memory[i-2])

print(memory[n] % 10007 )