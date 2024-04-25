def addString(num1, num2):
    num1_int = int(num1)
    num2_int = int(num2)
    
    result = num1_int + num2_int
    
    return str(result)

num1 = "10"
num2 = "20"
result = addString(num1, num2)
print("حاصل جمع:", result)
