
def my_merge_few(*arg):

	final_list = []
	for g_list in arg:
		for elem in g_list:
			final_list.append(elem)
	return(final_list)


def merge_sort(array):

	if len(array) <= 1:
		return array

	middle = int(len(array) / 2)
	left_array = merge_sort(array[:middle])
	right_array = merge_sort(array[middle:])

	return merge(left_array,right_array)

def merge(left_array,right_array):

	result_array = []
	left = right = 0
	while (left < len(left_array) and right < len(right_array)):

		if left_array[left] < right_array[right]:
			result_array.append(left_array[left])
			left += 1
		else :
			result_array.append(right_array[right])
			right +=1

	result_array.extend(left_array[left:])
	result_array.extend(right_array[right:])
	return result_array



