input1 = "another line"

def find_next_to_last(string):
    arr = string.split(" ")
    if len(arr) == 1:
        print(string)
    else:
        print(arr[len(arr)-2])

print find_next_to_last(input1)
