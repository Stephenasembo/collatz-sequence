print('Enter a number')
num = int(input())
def collatz(num):
	print(str(num))
	if(num == 1):
		return
	elif(num % 2 == 0 and num != 0):
		return collatz(num // 2)
	else:
		return collatz(num * 3 + 1)

collatz(num)