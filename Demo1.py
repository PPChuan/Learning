def insertsort(arr, k):
    if k == 0:
        return
    insertsort(arr, k - 1)
    for i in range(k, 0, -1):
        if arr[i] < arr[i-1]:
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = temp


if __name__ == '__main__':
    arr = [4,9,5,21,64,87,54]
    insertsort(arr, len(arr)-1)
    print(arr)