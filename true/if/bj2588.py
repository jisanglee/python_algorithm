# a,b = map(int,input().split())
# b = list(map(int,str(b)))
# sum = 0
# b.reverse()
# for i in range(len(b)):
# 	x = (a*b[i])
# 	sum += (10**i) * (x)
# 	print(x)
# print(sum)

# 문제 출제에 3자리수라고 정의되어있다.
n1 = int(input())
n2 = str(input())
 
print(n1 * int(n2[2]))
print(n1 * int(n2[1]))
print(n1 * int(n2[0]))
print(n1 * int(n2))