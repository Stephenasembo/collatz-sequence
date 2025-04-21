print('Enter a number')

def collatz(num):
	print(str(num))
	if num == 1:
		return
	elif num % 2 == 0 and num != 0 :
		return collatz(num // 2)
	else:
		return collatz(num * 3 + 1)
	print('Please enter a number')

def main():
	try:
		num = int(input())
		collatz(num)
	except:
		print('Please enter a number')
		main()

main()
