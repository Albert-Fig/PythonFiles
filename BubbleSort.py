def bubble_sort(arr):

    length = len(arr)
    for i in range(length-1):
       for j in range(length-i-1):
           if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    
    return arr




if __name__ == '__main__':
    li = [3, 4, 2, 1]
    li_sort = bubble_sort(li)
    print(li_sort)


pass