#my_str_len
def my_str_len(s):
    count = 0
    for char in s:
        count += 1
    return count
print(my_str_len("hello"))
print(my_str_len(""))

def my_max(lst):
    if len(lst) == 0:
        return None  

    max_value = lst[0]
    for element in lst[1:]:
        if element > max_value:
            max_value = element
    return max_value

# My_max 
print(my_max([3, 5, 1, 7, 2]))  
print(my_max([58, 37, 22, 1044]))

#Test my_str_len
print ("Test my_str_len")
print(my_str_len("Universitetet i Agder"))
print(my_str_len("Ballbasis"))
print(my_str_len("1"))

#Test max_value
print ("Test my_max")
print(my_max([3, 3, 68+11, 4, 66]))
print(my_max([3, 99, 68+11, 88, 500-200]))
print(my_max([3, 5, 8, 4, 11]))