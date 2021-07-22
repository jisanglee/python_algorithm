n = 1260
count = 0
#큰 단위의 화폐부터 차례로 확인
arr = [500,100,50,10]

for coin in array:
	count += n // coin #해당 화폐로 거슬로 줄 수 있는 동전 개수 세기
	n %= coin #거슬러주고 남은 돈

print(count)