from stack import Stack
from queue import Queue

N = 6

my_stack = Stack(N)
my_stack.push("Australia")
my_stack.push("India")
my_stack.push("Costa Rica")
my_stack.push("Preu")
my_stack.push("Ghana")
my_stack.push("Indonesia")

my_queue = Queue(N)
my_queue.enqueue("Australia")
my_queue.enqueue("India")
my_queue.enqueue("Costa Rica")
my_queue.enqueue("Peru")
my_queue.enqueue("Ghana")
my_queue.enqueue("Indonesia")

#Print the first values in the stack and queue
print("The top value in my stack is: {0}".format(my_stack.peek()))
print("The front value of my queue is: {0}".format(my_queue.peek()))


#Get First Value added to Queue
first_value_added_to_queue = my_queue.dequeue()
print("\nThe first value enqueued to the queue was {0}".format(first_value_added_to_queue))
queue_runtime = "1"
print("The runtime of getting the front of the queue is O({0})".format(queue_runtime))

#Get First Value added to Stack
#Write loop here!
while not my_stack.is_empty():
    first_value_added_to_stack = my_stack.pop()
print("\nThe first value pushed onto the stack was {0}".format(first_value_added_to_stack))
stack_runtime = "N"
print("The runtime of getting the bottom of the stack is O({0})".format(stack_runtime))

