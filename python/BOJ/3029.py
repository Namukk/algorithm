h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
t = t2 - t1 if t2 > t1 else t2-t1+24*60*60
h = t//60//60
m = t//60 % 60
s = t%60
print("%02d:%02d:%02d" % (h, m, s))

#https://jinho-study.tistory.com/484?category=911939


# 내가 하던거
# N = list(map(int, input().split(":")))
# T = list(map(int, input().split(":")))
# H = 0
# M = 0
# S = 0

# # second
# if N[2] >= T[2]:
#     S += (T[2]+60) - N[2]
#     M - 1
# else:
#     S += T[2] - N[2]
# # minute
# if N[1] >= T[1]:
#     M += (T[1]+60) - N[1]
#     H - 1
# else:
#     M += T[1] - N[1]
# # hour
# if N[0] > T[0]:
#     H += (24 - N[0]) + (T[0])
# elif N[0] == T[0]:
#     H = 0
# else:
#     H += T[0] - N[0]

# if M == 60:
#     M = 0
# if S == 60:
#     S = 0

# if H < 10:
#     H = "0"+str(H)
# if M < 10:
#     M = "0"+str(M)
# if S < 10:
#     S = "0"+str(S)


# print(H,":",M,":",S, sep="")
