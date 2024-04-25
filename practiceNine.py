def movSefr(lst):
    non_zero = []
    
    for num in lst:
        if num != 0:
            non_zero.append(num)
    
    zero_count = len(lst) - len(non_zero)
    non_zero.extend([0] * zero_count)
    
    return non_zero

input_list = [1, 0, 3, 4, 0, 0, 7, 5, 0, 6]
output_list = movSefr(input_list)
print("Output:", output_list)
