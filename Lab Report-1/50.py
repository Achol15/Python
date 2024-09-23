def remove_dup(input_list):
    return list(set(input_list))
input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
print("Original List: ", input_list)
print("List after removing duplicates: ", remove_dup(input_list))