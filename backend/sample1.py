def main():
	i = 5
	while (i > 0):
		print("i == " ,i)
		i -= 1
		while (i > 2):
			break
		if i == 1: break
if __name__ == "__main__":
	main()