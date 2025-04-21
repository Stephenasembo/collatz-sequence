def collatz(num):
	if num % 2 == 0 and num != 0:
		num = num // 2
	else:
		num = num * 3 + 1
	print(num)
	return num

def main():
	while True:
		try:
			print('Enter a valid integer')
			num = int(input())
			break
		except ValueError:
			print('Invalid input please try again.')
	while num != 1:
		num = collatz(num)

main()
