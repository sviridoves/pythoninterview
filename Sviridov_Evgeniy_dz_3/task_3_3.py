def make_dic(keys, values):
    len_keys = len(keys)
    len_values = len(values)
    if len_keys > len_values:
        for _ in range(len_keys - len_values):
            values.append(None)
    elif len_keys > len_values:
        for _ in range(len_values - len_keys):
            values.pop(-1)
    return {k: v for k, v in zip(keys, values)}


keys = [1, 2, 3, 5, 6, 4]
values_1 = ['a', 'b', 'c']
values_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
new_dic_1 = make_dic(keys, values_1)
print(new_dic_1)
new_dic_2 = make_dic(keys, values_2)
print(new_dic_2)
