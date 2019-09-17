def binary_search(value, lst):
	"""Binary search of value in sorted list"""
	low = 0
	high = len(lst)
	while low < high:
		index = int((low + high)/2)
		if lst[index] == value:
			return index
		elif lst[index] > value:
			high = index
		else:
			low = index
	return None 
if __name__ == '__main__':
    result = binary_search(2, range(1500))
    print(result)
