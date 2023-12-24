# create unsorted list
my_list = []
for i in range(10, 0, -1):
    my_list.append(i)
print('Before sort', my_list)

# actual code
for j in range(1, len(my_list), 1):
    key = my_list[j]
    i = j - 1
    while i > -1 and my_list[i] > key:
        my_list[i + 1] = my_list[i]
        i -= 1
    my_list[i + 1] = key

# print sorted list
print("my_list after sort:", my_list)
