def factorial_iteratove(n):
	result = 1
	for i in range(1,n+1):
		result = result * i
	return result
def factorial_recursive(n):
	if n<=1:
		return 1
	#n! = n*(n-1)!를 그대로 코드로 작성
	return n * factorial_recursive(n-1)

print(factorial_iteratove(5))
print(factorial_recursive(5))