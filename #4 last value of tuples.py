def replace_last_value(lst, value):
    return [tuple(lst[i][:-1]) + (value,) for i in range(len(lst))]

# sample list
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# replacing last value with 1000
new_lst = replace_last_value(lst, 1000)

# printing the new list
print(new_lst)
