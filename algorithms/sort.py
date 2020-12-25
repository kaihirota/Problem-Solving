def bubbleSort(array):
    for i in range(len(array)):
		for j in range(len(array)-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array

def insertionSort(array):
    for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i] > array[j]:
				tmp = array.pop(j)
				array.insert(i, tmp)
	return array

def selectionSort(array):
    for i in range(len(array)):
        minimum = (array[i], i)
        for j in range(i+1, len(array)):
            minimum = min(minimum, (array[j], j), key=lambda x: x[0])
        tmp = array.pop(minimum[1])
        array.insert(i, tmp)
    return array
