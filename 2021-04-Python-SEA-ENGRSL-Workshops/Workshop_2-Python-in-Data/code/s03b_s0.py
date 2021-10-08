def get_index_of(sequence, item):

	for i in range(len(sequence)):
		if sequence[i] == item:
			return i

numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
thirteenIndex = get_index_of(numbers, 13)
print("13 is at:", thirteenIndex)
