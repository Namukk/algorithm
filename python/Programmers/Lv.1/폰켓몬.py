def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums.sort()
    last = 0
    
    for i in nums:
        if(i != last and answer < length):
            answer += 1
            last = i
    
    return answer


# def solution(nums):
#     answer = 0
#     pick = len(nums) / 2
#     nums = list(set(nums))

#     if len(nums) >= pick:
#         answer = pick
#     elif len(nums) < pick:
#         answer = len(nums)

#     return answer