def firstUChar(string):
    char_count = {}
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for index, char in enumerate(string):
        if char_count[char] == 1:
            return index
    
    return -1

string = "hello"
print("Index of first non-repeating character:", firstUChar(string))
