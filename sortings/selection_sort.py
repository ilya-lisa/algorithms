# sorts an array arr with selection sort method
def sort(arr):
    for i in reversed(range(1, len(arr))):
        max_ndx = 0
        for j in range(i + 1):
            if arr[j] > arr[max_ndx]:
                max_ndx = j
        temp = arr[i]
        arr[i] = arr[max_ndx]
        arr[max_ndx] = temp
        print(max_ndx, end=' ')
    return arr

with open('/home/ipatrikeev/dev/input.txt') as f:
    f.readline()
    values = [int(x) for x in f.readline().split()]
    sort(values)
