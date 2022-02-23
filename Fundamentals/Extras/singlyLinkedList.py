class SList: #creates a singly linked list
    def __init__(self):
        self.head = None
    # Method to add a node to the front of a list
    def add_to_front(self, val):
            new_node = SLNode(val)	# Creates a new instance of our Node class using the given value
            print(new_node)
            #current_head = self.head  # Saves as the surrent head - sets the node to head when added to the front
            new_node.next = self.head # Sets the new node's next to the lists current head
            self.head = new_node  # Set's the list head to the node that is created (must be last step!)
            return self  # Must be included in order to chain methods together
    # Method to traverse through a list
    def print_values(self): 
        runner = self.head  # Pointer to the lists's head (first node)
        while (runner != None):  # While loop to iterate through the nodes in a list until the iterator does not have a neighbor
            print(runner.value)  # Prints the current node's value
    # Method to traverse through a list and add a value at the end
    def add_to_back(self, val):
        new_node = SLNode(val) 	# Creates a new instance of our Node class using the given value
        runner = self.head # Pointer to the lists's head (first node)
        while (runner.next != None):  # While loop to iterate through the nodes in a list until the iterator does not have a neighbor
            runner = runner.next  # Increment the runner to the next node in the list
        runner.next = new_node  #  Adds created node to the end of the list
        return self
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None #set self.next to none when it is the only/last item in the list


my_list = SList()  #creates an instance of a list
# my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

my_list.add_to_front("are")
