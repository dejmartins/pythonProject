# def rotate(my_list, x):
#     count = 0
#     while count < x:
#         last_item = my_list.pop()
#         my_list.insert(0, last_item)
#         print(my_list)
#         count += 1
#
#
# lst = [1, 2, 3, 4, 5]
# rotate(lst, 2)


def rotate(my_lst, k):
    return my_lst[-k:] + my_lst[:-k]

lst = [1, 2, 3, 4, 5]
print(rotate(lst, 3))
