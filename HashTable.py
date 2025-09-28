class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = -1

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        initial_index=self.hash_function(key)
        index=initial_index
        # if self.table[index] is not None and self.table[index] != self.deleted:
        #     if self.table[index] == key:
        #         print(f"Key {key} already exists at index {index}")
        #         return
        #     index = (index + 1) % self.size
        #     if index == initial_index:
        #         print("Hash table is full unable to insert key")
        #         return
        # self.table[index] = key
        # print(f"Key {key} inserted at index {index}")
        while self.table[index] is not None and self.table[index] != self.deleted:
            if self.table[index] == key:
                print(f"Key_{key}_already exists at index {index}")
                return
            index = (index + 1) % self.size
            if index == initial_index:
                print(f"Hash table is full unable to insert key {key}")
                return
        self.table[index] = key
        print(f"key_{key}_inserted at index {index}")

    def search(self, key):
        initial_index = self.hash_function(key)
        index = initial_index
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key_{key}_found at index {index}")
                return index
            index = (index + 1) % self.size
            if index == initial_index:
                break
            print(f"Key_{key}_not found")
            return -1

    def delete(self , key):
        initial_index = self.hash_function(key)
        index = initial_index
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index]=self.deleted
                print(f"key_{key}_deleted from index{index}")
                return
            index = (index + 1) % self.size
            if index == initial_index:
                break
            print(f"Key_{key}_not found")

    def display(self):
        print("___HASH TABLE___")
        for i , value in enumerate(self.table):
            if value==self.deleted:
                print(f"index{i}:DELETED")
            else:
                print(f"index{i}::{value}")

size=int(input("Enter the size of hash table:"))
if size<=0:
    print("Invalid size.")
else:
    hashtable = HashTable(size)
    while True:
        print("\n--- MENU ---")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key to insert: "))
            hashtable.insert(key)
        elif choice == 2:
            key = int(input("Enter key to search: "))
            hashtable.search(key)
        elif choice == 3:
            key = int(input("Enter key to delete: "))
            hashtable.delete(key)
        elif choice == 4:
            hashtable.display()
        elif choice == 5:
            print("Exit!!.")
            break
        else:
            print("Invalid choice.")

