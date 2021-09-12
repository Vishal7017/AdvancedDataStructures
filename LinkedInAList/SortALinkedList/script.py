from linkedlist import LinkedList

def find_max(linked_list):
    current = linked_list.get_head_node()
    maximum = current.get_value()
    while current.get_next_node():
        current = current.get_next_node()
        val = current.get_value()
        if val > maximum:
            maximum = val
    return maximum


def sort_linked_list(linked_list):
    print("\n--------------------------")
    print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
    new_linked_list = LinkedList()

    while linked_list.get_head_node():
        current_max = find_max(linked_list)
        linked_list.remove_node(current_max)
        new_linked_list.insert_beginning(current_max)
    
    return new_linked_list


#Test Cases

ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))


ll_2 = LinkedList(1)
ll_2.insert_beginning(43)
ll_2.insert_beginning(23)
ll_2.insert_beginning(32)
ll_2.insert_beginning(4)
ll_2.insert_beginning(54)
print("The sorted linked list is:\n".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(3294)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-45)
ll_3.insert_beginning(4345)
print("The sorted linked list is :\n{0}".format(sort_linked_list(ll_3).stringify_list()))


#Runtime
runtime = "N^2"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))