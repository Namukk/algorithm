N, T = map(int, input().split())

a = list(map(int, input().split()))
a = sorted(a)

print(a[T-1])

# pypy3 이용해야 정답


# 다른 정답
# https://assaeunji.github.io/python/2020-05-06-bj11004/    참고

# def merge_sort(array):
#     if len(array)<=1:
#         return array
#     mid = len(array) // 2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])

#     i,j,k = 0,0,0

#     while i < len(left) and j <len(right):
#         if left[i] < right[j]:
#             array[k] = left[i]
#             i += 1
#         else:
#             array[k] = right[j]
#             j += 1
#         k+=1
    
#     if i==len(left):
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
#     elif j==len(right):
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
#     return array

# # 데이터 입력
# n,k = map(int,input().split())

# num = list(map(int, input().split()))
# num = merge_sort(num)

# print(num[k-1])