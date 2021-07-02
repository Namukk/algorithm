A, B = map(int, input().split())
# 2와 5의 개수만 맞으면 됨. (그러면 10의 배수)   밑은 확인 함수
def five_count(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

def two_count(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer

if B == 0:
    print(0)
    
else:       
    print(min(two_count(A)-two_count(B)-two_count(A-B), five_count(A)-five_count(B)-five_count(A-B)))


# https://claude-u.tistory.com/242   답 참고