t = int(input())

arr = []

for i in range(t):
  arr.append(input())

def is_palin(str):

  left, right = 0, len(str) - 1

  while left < right:

    if str[left] == str[right]:
      left += 1
      right -= 1

    else:
      if left < right - 1:
        str_temp = str[:right] + str[right + 1:]

        if str_temp[:] == str_temp[::-1]:
          return 1

      if left + 1 < right:
        str_temp = str[:left] + str[left+1:]

        if str_temp[:] == str_temp[::-1]:
          return 1
      return 2

for i in arr:
  if is_palin(str(i)) == None:
    print(0)
  else:
    print(is_palin(str(i)))
  