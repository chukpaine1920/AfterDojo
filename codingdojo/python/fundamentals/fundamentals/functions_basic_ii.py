
#countdown
def countdown(num):
    output = []
    for i in range(num, -1, -1):
        output.append(i)
    return output

# print(countdown(9))

print and return
def print_and_return(list):
    print(list[0])
    return(list[1])

# print(print_and_return([1,2]))


# first plus length
def first_plus_len(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

#values greater than second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


#this length, that value
def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))