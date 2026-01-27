class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued to queue.")
    def dequeue(self):
        if not self.isempty():
            ritem = self.queue.pop(0)   # remove from front
            print(f"{ritem} dequeued from queue.")
            return ritem
        else:
            print("Queue is empty! Cannot dequeue an element.")
            return None
    def isempty(self):
        return len(self.queue) == 0
    def display(self):
        if not self.isempty():
            print("Queue elements from front to rear:")
            for item in self.queue:
                print(item, end=" ")
            print()
        else:
            print("Queue is empty!")
q = Queue()
while True:
    print("\nMenu:")
    print("1. Enqueue element to queue")
    print("2. Dequeue element from queue")
    print("3. Display queue")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter the value to enqueue into the queue: "))
        q.enqueue(item)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please select a valid option.")
