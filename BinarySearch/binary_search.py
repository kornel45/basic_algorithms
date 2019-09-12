def binary_search(value, lst):
	"""Binary search of value in sorted list"""
	how_many = 0
	low = 0
	high = len(lst)
	while low < high:
		how_many += 1
		index = int((low + high)/2)
		if lst[index] < value:
			low = index
		elif lst[index] > value:
			high = index
		else:
			return index, how_many
	return -1, how_many

x = binary_search(10, list(range(1500)))
print(x)

