class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.name}: {self.number}'

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size


    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size


    def insert(self, key, value):
        contact = Contact(key, value)
        index = self.hash_function(key)
        current_node = self.data[index]

        if current_node == None: #empty index
            self.data[index] = Node(key, contact)
            return

        else: #occupied index
            while current_node != None:
                if current_node.key == key: #update existing key
                    current_node.value = contact
                    return
                
                else:
                    if current_node.next == None: #end of list
                        current_node.next = Node(key, contact)
                        return

                    else: #keep going down list
                        current_node = current_node.next


    def search(self, key):
        index = self.hash_function(key)
        current_node = self.data[index]

        while current_node != None:
            if current_node.key == key:
                return current_node.value 

            else:
                current_node = current_node.next

        return None


    def print_table(self):
        index = 0
        for entry in self.data:
            if entry == None:
                print(f'Index {index}: Empty')

            else:
                print(f'Index {index}:', end = "")
                current_node = entry
                while current_node != None:
                    print(f' - {current_node.value}', end = "")
                    current_node = current_node.next

                print("")

            index += 1

        print("")


# Test your hash table implementation here. 
#Empty table
print("Empty table:")  
table = HashTable(10)
table.print_table()

#two values, no collisions
print("No-collision insertion:")
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.print_table()

#searching
print("Searching: ")
contact = table.search("John") 
print(f'Search result: {contact}') 
print("")

#collision
print("Inserting with collision:")
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  
table.print_table()

#duplicate
print("Updating existing contact:")
table.insert("Rebecca", "999-444-9999")
table.print_table()

#Non-existant
print("Searching for non-existant value")
print(table.search("Chris"))




"""
At the bottom of your file or in a separate .txt file, include a short reflection (200–300 words) that answers the following:

    Why is a hash table the right structure for fast lookups?
        A hash table is the right structure for fast lookups because it can jump straight to the index an item is stored at instead of traversing. As long as the hash function being used and the values being used as keys don't tend to create an excess of collisions, the vast majority of data in the list does not need to be dealt with in order to find the location of an entry, and instead can be accessed directly in O(1) time. 
    How did you handle collisions?
        Collisions are handled by having each index be a singly linked list so that inserted values that have a collision can be placed at the back of the list. This allows multiple values to be at the same index without spilling into other indexes, but can also slow down the time needed to access values at that index.
    When might an engineer choose a hash table over a list or tree?
        A hash table might be chosen over a list or tree when the data being stored: needs to be accessed quickly, does not need to be ordered, and has property well suited to being used as a key. Because hash tables are optimized for lookup speed above everything, they also take up more space compared to a list or tree, so they might be chosen typically only when storage is not being pressured.


"""