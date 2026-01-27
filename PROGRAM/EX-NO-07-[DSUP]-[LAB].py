def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


n = int(input("Enter the number of elements in the list: "))
ll = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    ll.append(element)

value = int(input("Enter the value to search for: "))

pos = linear_search(ll, value)

if pos != -1:
    print(f"Value found at position {pos}.")
else:
    print("Value not found.")
