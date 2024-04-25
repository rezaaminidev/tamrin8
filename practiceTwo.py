def find_largest_value(input_list):
    max_value = None
    for item in input_list:
        if isinstance(item, str):
            if max_value is None or len(item) > len(max_value):
                max_value = item
        elif isinstance(item, int):
            if max_value is None or item > max_value:
                max_value = item
    return max_value


my_list = ['apple', 25, 'banana', 100, 'orange', 50]
largest_value = find_largest_value(my_list)
print("Bigger value:", largest_value)
