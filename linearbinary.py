def linear_search(n, L, target):
    
    for i in range (0,n):
        if L[i] == target:
            return True
    return False
def binary_search(n, target):
    n.sort()
    low = 0
    high = len(n) - 1
    while low <= high:
        mid = (low + high) // 2
        if n[mid] == target:
            return True
        elif n[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
L1 = []
n= int(input("Enter the number of Account ID's:"))
for i in range(0,n):
    ele = int(input("Enter the Account ID:"))
    L1.append(ele)

while True:
    print("\n\n_MENU")
    print("1.Enter account ID to be searched:")
    print("2.Linear search:")
    print("3.Binary search:")
    print("4.Exit:")
    choice=int(input("Enter choice_1-4:"))
    if choice==1:
        print(L1)
        target_id = int(input("Enter customer account ID to search: "))
    elif choice==2:
        if linear_search(n, L1, target_id):
            print("Linear Search: Account ID found at index:",i)
        else:
            print("Linear Search: Account ID not found.")
            
    elif choice==3:
        if binary_search(L1, target_id):
            print("Binary Search: Account ID found at index:",i)
        else:
            print("Binary Search: Account ID not found")
    elif choice==4:
        print("Exit The Loop!")
        break
    else:
        print("invalid input")