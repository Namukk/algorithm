N = int(input())
S = []
L = []
count = 1
temp = True

for i in range(N):
    num = int(input())
    while count <= num:
        S.append(count)
        L.append('+')
        count += 1
    if S[-1] == num:
        S.pop()
        L.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in L:
        print(i)

# https://pacific-ocean.tistory.com/231   답 참고