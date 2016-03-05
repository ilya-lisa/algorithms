def top_down_sort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    ndx = 0
    for elem in arr:
        if ndx % 2 == 0:
            right.append(elem)
        else:
            left.append(elem)
        ndx += 1
    left = top_down_sort(left)
    right = top_down_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    left_ndx = 0
    right_ndx = 0
    while left_ndx < len(left) and right_ndx < len(right):
        if left[left_ndx] < right[right_ndx]:
            result.append(left[left_ndx])
            left_ndx += 1
        else:
            result.append(right[right_ndx])
            right_ndx += 1

    if left_ndx < len(left):
        for i in range(left_ndx, len(left)):
            result.append(left[i])
    elif right_ndx < len(right):
        for i in range(right_ndx, len(right)):
            result.append(right[i])

    return result

