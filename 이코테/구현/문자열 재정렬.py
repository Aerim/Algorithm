
i = input()

number=0
alphabet=[]

ap_alphabet=''

temp=[str(n) for n in range(0,10)]

# 0~9까지 숫자가 입력에 존재하면 더하기
for j in i:
    if j in temp:
        number+=int(j)
# 아니면 알파벳 리스트에 삽입
    else: 
        alphabet.append(j)

alphabet.sort()

for k in alphabet:
    ap_alphabet+=k

# 더한값이 0이상이면 숫자까지 출력
if number>0: print(ap_alphabet+str(number))
else: print(ap_alphabet)