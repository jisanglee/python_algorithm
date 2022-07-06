# 3이 1개라도 ?
N = int(input())
count = 0
#내풀이
# for i in range(N+1):
#     if i == 3 or i == 13 or i == 23:
#         count += 3600
#     else:
#         count += 1575

#책 정답
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)