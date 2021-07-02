N = int(input())
answer = []

while N != 1:
    for i in range(2, N + 1):
        if N % i == 0:
            answer.append(i)
            N //= i
            break

for j in answer:
    print(j)

# https://devuna.tistory.com/32