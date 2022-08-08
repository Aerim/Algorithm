n, m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

answer = []

a_pointer , b_pointer = 0, 0 
a_len, b_len = len(a), len(b)

while a_pointer != a_len or b_pointer != b_len:
    if a_pointer == a_len:
        answer.append(b[b_pointer])
        b_pointer += 1

    elif b_pointer == b_len:
        answer.append(a[a_pointer])
        a_pointer += 1
    else:
        if a[a_pointer] < b[b_pointer]:
            answer.append(a[a_pointer])
            a_pointer += 1

        else:
            answer.append(b[b_pointer])
            b_pointer += 1

print(*answer)