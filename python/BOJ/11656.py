N = str(input())
L = []

for i in N:
    L.append(N)
    N = N[1:]

for j in sorted(L):
    print(j)


# https://claude-u.tistory.com/284   답 참고

# https://o-sae.tistory.com/77     이런 방법도
# S = input()

# suffix = []
# for i in range(len(S)) :
#     suffix.append(S[i:])

# suffix.sort()
# for i in suffix :
#     print(i)