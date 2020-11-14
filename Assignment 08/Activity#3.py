N = 10
fibonacci = [0,1]
if N>2:
	for i in range(2, N):
		fib = fibonacci[i-1] + fibonacci[i-2]
		fibonacci.append(fib)
print(fibonacci)
