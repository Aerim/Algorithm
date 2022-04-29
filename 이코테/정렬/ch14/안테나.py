n = int(input())

an = list(map(int,input().split()))
an = sorted(an)

if len(an) % 2 == 0:
    print(an[len(an)//2-1])
else:
    print(an[len(an)//2])