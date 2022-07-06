#큰수의 법칙pg92
N,M,K = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
Bnum = data[N-1]
Snum = data[N-2]
print((Bnum*K + Snum)*int(M/(K+1)) + Bnum*(M%(K+1)))