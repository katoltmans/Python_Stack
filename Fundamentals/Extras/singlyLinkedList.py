class SList: #creates a singly linked list
    def __init__(self):
        self.head = None
        
    def add_to_front(self, val):
            new_node = SLNode(val)	# create a new instance of our Node class using the given value
