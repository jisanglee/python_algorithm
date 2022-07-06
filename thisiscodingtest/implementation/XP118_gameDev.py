N,M = map(int,input().split())
X,Y,D = map(int,input().split())

arr = []
for _ in range(N):
	arr.append(list(map(int,input().split())))
map = [[0] * M for _ in range(N)]

#입력안받고 더미 테스트 데이터
# X=1
# Y=1
# M,N = 4,4
# D = 0
# arr = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

#현재 방향을 기점으로 방향체크하기 (1,1)에서 북을 봤을땐 (0,1)이므로 북은 -1,0 따라서 dx[0] = -1 dy[0] = 0 왼쪽으로 돌아가므로 북 서 남 동 이순으로 가야함
#1,1,1,1
#1,0,0,1
#1,1,0,1
#1,1,1,1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

#방향구하기
def turn_left():
	global D
	D -= 1
	if D == -1:
		D = 3

turn_time = 0
#현재 맵 체크하고 카운트는 1부터 시작
map[X][Y] = 1
count= 1
while True:
	#왼쪽으로 회전
	turn_left()
	nx = X + dx[D]
	ny = Y + dy[D]

	if map[nx][ny] == 0 and arr[nx][ny] == 0:
		map[nx][ny] = 1
		X = nx
		Y = ny
		count +=1 
		turn_time = 0
		continue
	#회전 한 이후 정면에 가보지 않은 칸이 없거나 바다인경우
	else:
		turn_time +=1
	#네방향 다 갈 수 없는 경우
	if turn_time == 4:
		nx = X-dx[D]
		ny = Y-dy[D]
		#뒤로 갈 수 있다면 이동하기
		if arr[nx][ny] == 0:
			X = nx
			Y = ny
		#뒤가 바다로 막혀 있는 경우
		else:
			break
		turn_time = 0
print(count)