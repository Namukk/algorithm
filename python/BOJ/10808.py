N = list(str(input()))
L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(len(L)):
    a = N.count(L[i])
    print(a, end=" ")


# https://oort-cloud.tistory.com/32   참고

# https://jinho-study.tistory.com/175
# li = [0]*26
# for c in input():
#       li[ord(c)-ord('a')] += 1
# print(*li)

#https://yuuj.tistory.com/147     -아스키
# import sys

# word = sys.stdin.readline().strip()
# arr = [0 for _ in range(26)]

# for each in word:
#     arr[ord(each)-97] += 1

# print(" ".join(map(str, arr)))

