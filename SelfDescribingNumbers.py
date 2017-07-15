
number1 = 1210

def count_occurences(number):
    string = str(number)
    arr = [0,0,0,0,0,0,0,0,0,0]
    for c in string:
        found_digit = int(c)
        arr[found_digit] += 1
    return arr

def is_happy(number):
    ishappy = 1
    arr = count_occurences(number)
    string = str(number)
    for x in range(0, len(string)-1):
        char = string[x]
        if int(char) != arr[x]:
            ishappy = 0
    return ishappy

print is_happy(number1)
