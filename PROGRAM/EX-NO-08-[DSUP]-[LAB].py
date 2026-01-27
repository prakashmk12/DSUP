def binary_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        midvalue = a[mid]
        if midvalue == x:
            return mid
        elif midvalue < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
n = int(input("Enter the number of elements in the sorted list: "))
sortlist = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    sortlist.append(element)
x = int(input("Enter the target value to search for: "))
pos = binary_search(sortlist, x)
if pos != -1:
    print(f"Value found at index {pos}.")
else:
    print("Value not found.")
