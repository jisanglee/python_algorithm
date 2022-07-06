#LRUD
N = int(input())
lrud = input().split()
H = 1
W = 1
# for i in lrud:
# 	if i =='L':
# 		if W != 1:W-=1
# 	elif i == 'R':
# 		if W != N:W+=1
# 	elif i == 'U':
# 		if H != 1:H-=1
# 	elif i == 'D':
# 		if H != N:H+=1
# print(f'{H} {W}')
move_types = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for lrud in lruds:
	for i in range(len(move_types)):
		if lrud == move_types[i]:
			nx = X + dx[i]
			ny = Y + dy[i]
	if nx < 1 or ny < 1 or nx > N or ny > N :
		continue
	X,Y = nx,ny
print(f'{X} {Y}')