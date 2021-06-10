

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


def partition(arr, left, right):
	pivot = arr[right]
	i = left-1
	for j in range(left, right):
		if arr[j] <= pivot:
			i += 1
			swap(arr, i, j)
	swap(arr, i+1, right)
	return i+1


def quick_sort(arr, left, right):
	if left < right:
		pivot = partition(arr, left, right)
		quick_sort(arr, left, pivot-1)
		quick_sort(arr, pivot+1, right)


if __name__ == '__main__':
	li = [4, 3, 2, 1]
	quick_sort(li, 0, len(li)-1)
	print(li)
	pass


pass
