class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


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
        self.buckets = [None] * capacity
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
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.capacity

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
        # Your code here
        hash = 5381

        for char in key:
            hash = (hash * 33) + ord(char)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % len(self.buckets)


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.buckets[index]

        # if current slot is empty, make new entry with the key and value
        if current is None:
            self.buckets[index] = HashTableEntry(key, value)
            self.size += 1
            return

        # if there is something in the current slot    
        while current is not None:
            # if it's equal to the key, overwrite the current value with the new one
            if current.key == key:
                current.value = value
                break

            # if current has a next entry, set the current to the currents next entry
            if current.next:
                current = current.next

            # if current has no next and is not key, create a new entry in its position
            if current.next is None and current.key is not key:
                current.next = HashTableEntry(key, value)
                self.size += 1
                break


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        index = self.hash_index(key)
        current = self.buckets[index]
        
        # if "head" is None
        if current is None:
            return None

        # if "head" is current key
        if current.key == key:
            # if there is .next assign current.next as the new "head"
            if current.next:
                self.buckets[index] = current.next
                self.size -= 1
            else:
                self.buckets[index] = None
                self.size -= 1

            
        else:
            # while there is something in the slot
            while current is not None:
                if current.next.key is key:
                    # if the "heads" next is equal to key and its next also has a next, set the current next as the next's next
                    if current.next.next:
                        current.next = current.next.next
                        self.size -= 1
                        break
                    else:
                        current.next = None
                        self.size -= 1
                        break
                else:
                    # if current is not equal to key, set current as it's next
                    current = current.next



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        
        index = self.hash_index(key)
        current = self.buckets[index]
        
        # if current slot has nothing, return None
        if current is None:
            return None
        
        # if something is in the slot
        while current is not None:
            # if the current entry is equals to the key, return current value
            if current.key == key:
                return current.value

            # if current has a next, set current as the old currents next
         
            current = current.next

            # if current has no next and the current entry is not equals to the key, return None
            # if not current.next and current.key is not key:
        return None
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        currentBuckets = self.buckets

        if new_capacity is None:
            if self.get_load_factor >= 0.7:
                self.capacity *= 2
                self.buckets = [None] * self.capacity

                for entry in currentBuckets:
                    self.put(entry.key, entry.value)

            if self.get_load_factor <= 0.2:
                self.capacity /= 2
                self.buckets = [None] * self.capacity

                for entry in currentBuckets:
                    self.put(entry.key, entry.value)


        else:
            self.capacity = new_capacity
            self.buckets = [None] * self.capacity

            for entry in currentBuckets:
                while entry is not None:
                    self.put(entry.key, entry.value)
                    entry = entry.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
