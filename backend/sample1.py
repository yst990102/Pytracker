def main():
	even_sum = 0
	odd_sum = 0
	i = 0
	while i < 4:
		j = 4
		while j < 6:
			if (i + j) % 2 == 0:
				even_sum += (i + j)
			else:
				odd_sum += (i + j)
			j += 1 
		i += 1
	
	print(even_sum)
	print(odd_sum)

if __name__ == "__main__":
	main()