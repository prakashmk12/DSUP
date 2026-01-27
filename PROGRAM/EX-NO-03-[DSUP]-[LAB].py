class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(str(item) + " pushed to Stack.")

    def pop(self):
        if not self.isempty():
            ritem = self.stack.pop()
            print(str(ritem) + " popped from Stack.")
            return ritem
        else:
            print("Stack is empty! Cannot pop an element.")
            return None

    def isempty(self):
        return len(self.stack) == 0

    def display(self):
        if not self.isempty():
            print("Stack elements from top to bottom:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty!")


# Main Program
s = Stack()

while True:
    print("\nMenu:")
    print("1. Push element to Stack")
    print("2. Pop element from Stack")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter the value to push onto the Stack: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please select a valid option.")
