import math


def merge_sort(a, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

    return a


def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)
    for i in range(n1):
        left[i] = a[p + i]
    for j in range(n2):
        right[j] = a[q + j + 1]

    left[n1] = float('inf')  # Adding sentinels to mark the end of array
    right[n2] = float('inf')  # Adding sentinels to mark the end of array

    i = 0
    j = 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1


# create unsorted list
my_list = []
for i in range(10, 0, -1):
    my_list.append(i)
print('Before sort', my_list)

# call function
merge_sort(my_list, 0, len(my_list) - 1)

# print sorted list
print('After sort', my_list)
