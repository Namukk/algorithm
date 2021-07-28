import sys
N = sys.stdin.readline().strip()

stackA = []
stackB = []
t = 1
temp = True
answer = 0

for i in range(len(N)):
    if N[i] == "(":
        stackA.append(i)
        t *= 2
    elif N[i] == "[":
        stackB.append(i)
        t *= 3
    elif N[i] == ")":
        if stackA:
            if N[i-1] == "(":
                answer += t
            stackA.pop()
            t //= 2
        else:
            temp = False
            break
    elif N[i] == "]":
        if stackB:
            if N[i-1] == "[":
                answer += t
            stackB.pop()
            t //= 3
        else:
            temp = False
            break
if not stackB and not stackA and temp:
    print(answer)
else:
    print(0)


# https://namhandong.tistory.com/141    답 참고
# https://jiwon-coding.tistory.com/89