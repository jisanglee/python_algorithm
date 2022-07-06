N,K = map(int,input().split())
count = 0
#단순하게 
# while(1):
# 	if N % K == 0:
# 		N/=K
# 		count+=1
# 	elif N == 1:
# 		break
# 	else:
# 		N-=1
# 		count+=1

#최대한 연산을 단순하게
while(N>=K):
	count += N % K
	N-=N%K
	if N < K:
		break
	N //= K
	count +=1


if N>1:
	count += N-1

	
print(int(count))

