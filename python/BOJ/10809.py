N = list(str(input()))
L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(len(L)):
    if L[i] not in N:
        print(-1, end=" ")
    else:
        print(N.index(L[i]), end=" ")


# https://gururuglasses.tistory.com/88 

# S = input()
# abc ='abcdefghijklmnopqrstuvwxyz'

# for i in abc:
#     if i in S:
#         print(S.index(i), end= ' ')
#     else:
#         print( -1, end =' ')

# https://yang-wistory1009.tistory.com/73    참고
# https://itprogramming119.tistory.com/entry/%EB%B0%B1%EC%A4%80%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-10809%EB%B2%88-%EC%95%8C%ED%8C%8C%EB%B2%B3-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython    참고