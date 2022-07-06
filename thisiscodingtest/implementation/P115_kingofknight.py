#왕실의 나이트 P115
N = input()
alp = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
X = alp[N[0]]
Y = int(N[1])

sum = 0
#좌상 좌하 우상 우하 상좌 상우 하좌 하우
ax = [2,2,-2,-2,1,-1,1,-1]
ay = [1,-1,1,-1,2,2,-2,-2]
for i in range(8):
	a = X + ax[i]
	b = Y + ay[i]
	if a < 1 or a >8 or b<1 or b>8:
		continue
	else:
		sum +=1
print(sum)
