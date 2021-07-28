N=int(input())
L = input()
nums=[0] * N
for i in range(N):
    nums[i]=int(input())
stack=[]

for i in L:
    if i.isupper():      
        stack.append(nums[ord(i)-ord('A')])
    else:
        num2=stack.pop()
        num1=stack.pop()
        if i=='+':
            stack.append(num1+num2)
        elif i=='-':
            stack.append(num1-num2)
        elif i=='/':
            stack.append(num1/num2)
        elif i=='*':
            stack.append(num1*num2)

print('%.2f' %stack[0])


# https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-1935%EB%B2%88-%ED%9B%84%EC%9C%84-%ED%91%9C%EA%B8%B0%EC%8B%9D2-%EC%B4%88%EC%BD%94%EB%8D%94   답 참고
# https://velog.io/@dailyhyun/BOJ%EB%B0%B1%EC%A4%80-1935.-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EC%8B%9D2   마지막 참고