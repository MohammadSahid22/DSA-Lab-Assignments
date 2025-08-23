def compute_average(records):
    total = sum(records.values())
    count = len(records)
    return(int(total / count))

def find_max_min(records):
    non_zero_values = [val for val in records.values() if val > 0]
    max_borrow = max(records.values())
    min_borrow = min(non_zero_values)
    return max_borrow, min_borrow

def count_zero_borrowers(records):
    return list(records.values()).count(0)

def find_mode(records):
    from collections import Counter
    non_zero_values = [val for val in records.values() if val > 0]
    freq = Counter(non_zero_values)
    most_common = freq.most_common(1)[0][0]
    return most_common

borrow_records = {
    'Alice': 3,
    'Bob': 0,
    'Charlie': 5,
    'David': 2,
    'Eve': 0,
    'Frank': 5,
    'Grace': 1
}
while True:

        print("\n--- Menu ---")
        print("1. Compute average number of books borrowed")
        print("2. Find book with highest and lowest borrowings")
        print("3. Count members who have not borrowed any books")
        print("4. Most frequently borrowed book excluding 0")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            average = compute_average(borrow_records)
            print("Average books borrowed:" ,average)
        
        elif choice == '2':
            max_borrow, min_borrow = find_max_min(borrow_records)
            print("Maximum books borrowed by any member:", max_borrow)
            print("Minimum books borrowed by any member (excluding zero):", min_borrow)
        
        elif choice == '3':
            zero_count = count_zero_borrowers(borrow_records)
            print("Members who borrowed 0 books:", {zero_count})
        
        elif choice == '4':
            mode_borrow = find_mode(borrow_records)
            print("Most frequently borrowed count (mode, excluding zero):", mode_borrow)
        
        elif choice == '5':
            print("Exiting the program...")
            break
            
        
        else:
          print("Invalid choice. Please try again.")