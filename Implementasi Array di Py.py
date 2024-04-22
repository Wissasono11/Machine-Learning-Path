#Mendeklarasi Array
var_list = [1,2,3]
for elemen in var_list:
    print(id(elemen))

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)
"""
Output:
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
var_arr = [0 for i in range(10)]
print(var_arr)
"""
Output:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""
var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i
print(var_arr)
"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
print("=== Mengakses Elemen Array ===")
var_arr = [9, 8, 7, 6, 5, 4, 3, 2 ,1, 0]
print(var_arr[0])
"""
Output:
9
"""
print("=== Pemrosesan Sekuensial pada Array ===")
var_arr = [1, 2, 3, 4, 5]
for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next element: {next_element}")

print("=== Latihan Array ===")
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
print(left_pointer)