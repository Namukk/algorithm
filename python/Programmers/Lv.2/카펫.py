def solution(brown, yellow):
    
    a = yellow
    b = brown
    
    T = (b + 4)//2
    K = 4 * (a + b)
    
    x = (T + (T ** 2 - K) ** 0.5) / 2
    y = (T - (T ** 2 - K) ** 0.5) / 2
    
    answer = [int(x), int(y)]
    
    
    return answer