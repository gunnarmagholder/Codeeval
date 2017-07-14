 
def returnDigits(input_number):
    input_string = str(input_number)
    return_array = []
    for c in input_string:
        return_array.append(int(c))
    return return_array
 
def sum_squares(input_number):
    int_array = returnDigits(input_number)
    sum = 0
    for i in int_array:
        sum += i*i
    return sum
 
def check_happy(input_number):
    iterations = []
    sum = sum_squares(input_number)   
    while ((sum != 1) and  (not (sum in iterations))):
        iterations.append(sum)
        sum = sum_squares(sum)
    if (sum == 1):
        print(1)
    else:
        print(0)

