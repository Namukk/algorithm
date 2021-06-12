# N = int(input())  이거 변수로 넣으면 왜 안됨?
A = []
for i in range(9):
    A.append(int(input()))
sum_A = sum(A)
one = 0
two = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum_A - (A[i] + A[j]) == 100:
            one = A[i]
            two = A[j]
A.remove(one)
A.remove(two)
A.sort()
for i in A:
    print(i) #왜 print(A[i])가 아닐까?