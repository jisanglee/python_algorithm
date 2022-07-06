#큰수찾기
N,M = map(int,input().split())
result = []
#행 포문(입력받기)
for i in range(N):
	data = list(map(int,input().split()))
	result.append(min(data))
print(max(result))
	
