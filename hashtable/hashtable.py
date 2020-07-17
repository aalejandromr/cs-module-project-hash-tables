class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 1

    def add_to_head(self, value):
        if self.head is None:
            node = Node(value)
        else:
            prev = self.head
            self.head = Node(value, prev)

        self.size =+ 1

    def remove_from_head(self):
        if self.head is None:
            return

        current_head = self.head
        new_head = current_head.next
        current_head = None
        self.head = new_head

        self.size =- 1

    def remove(self, value):
        current = self.head
        # if there is nothing to delete
        if current is None:
            return None
        # when deleting head
        if current.value[0] == value:
            self.head = current.next
            return current
        # when deleting something else
        else:
            previous = current
            current = current.next
            while current is not None:
                if current.value[0] == value: # found it!
                    previous.next = current.next  # cut current out!
                    return current # return our deleted node
                else:
                    previous = current
                    current = current.next
            return None # if we got here, nothing was found!

    def __len__(self):
        return self.size

    def __str__(self):
        current_node = self.head
        total = 0
        str = ""
        while current_node != None:
            str += f"index {total}: key => {current_node.value[0]}, value => {current_node.value[1]}\n"
            # str += f"index {total}: length {len(self)} \n"
            current_node = current_node.next
            total += 1
        return str
    # Remove from linked list


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = (( hash << 5) + hash) + ord(char)
        return hash
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % len(self.storage)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hashed_key = self.hash_index(key)
        if self.storage[hashed_key] != None:
            linkedList = self.storage[hashed_key]
            linkedList.add_to_head((key, value))
        else:
            self.storage[hashed_key] = LinkedList(Node((key, value)))
        # Your code here


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hashed_key = self.hash_index(key)
        if self.storage[hashed_key] == None:
            return None

        if len(self.storage[hashed_key]) >= 1:
            self.storage[hashed_key].remove(key)
        else:
            self.storage[hashed_key].head = None
        # Your code here


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hashed_key = self.hash_index(key)
        if self.storage[hashed_key] == None:
            return None

        if len(self.storage[hashed_key]) >= 1:
            current_head = self.storage[hashed_key].head

            while current_head != None:
                if current_head.value[0] == key:
                    return current_head.value[1]
                current_head = current_head.next
            return None
        else:
            return self.storage[hashed_key].head.value[1]
        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        value_key_pair = []
        # Get all key-value from store
        # Resize Storage
        # Calculate hash key and insert them in resized storage

        # Deep copy
        for store in self.storage:
            if len(store) >= 1:
                current_head = store.head
                while current_head != None:
                    value_key_pair.append(current_head.value)
                    current_head = current_head.next
            else:
                value_key_pair.append(store[0])
        # print(value_key_pair[0])
        self.storage = [None] * self.capacity

        for key_value in value_key_pair:
            self.put(key_value[0], key_value[1])

        # Your code here
if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))
    # return_value = ht.get("key-8")
    print(ht.storage[3])
    ht.delete("key-8")
    print(ht.storage[3])

    ht.resize(16)

    print(ht.storage)
    # ht.delete("key-6")
    # ht.delete("key-5")
    # ht.delete("key-4")
    # ht.delete("key-3")
    # ht.delete("key-2")
    # ht.delete("key-1")
    # ht.delete("key-0")

    # return_value = ht.get("key-8")
    # print(return_value)
    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")