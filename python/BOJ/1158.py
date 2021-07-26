N, M = map(int, input().split())
L = [ _+1 for _ in range(N)]
result = []
temp = M - 1

for i in range(N):
    if len(L) > temp:
        result.append(str(L.pop(temp)))
        temp += M-1
    elif len(L) <= temp:
        temp = temp % len(L)
        result.append(str(L.pop(temp)))
        temp += M-1

result_ = "<" + ", ".join(result) + ">"
print(result_)
# print("<",",".join(result)[:],">", sep='')


# https://claude-u.tistory.com/313   답 참고
# https://infinitt.tistory.com/213   이런것도