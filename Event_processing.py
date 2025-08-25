event = []

def add_event(event_name):
    event.append(event_name)
    print(f"Event added to queue:{event}")

def process_event():
    if event:
        x = event.pop(0)
        print(f"Event is processed:{x}")
    else:
        print("No Events Available For Processing")

def display_pending():
    if event:
        print("Pending events:")
        for i in event:
            print(i)
    else:
        print("No Pending Events")

def cancel_event(event_name):
    if event:
        event.remove(event_name)
        print(f"event is cancled:{event_name}")
    else:
        print("No Events Available or events are processed")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Add Event")
        print("2. Process Event")
        print("3. Display Pending Events")
        print("4. Cancel Event")
        print("5. Exit")
    
        choice = input("Enter your choice: ")
    
        if choice == '1':
            event = input("Enter event name to add: ")
            add_event(event)
        elif choice == '2':
            process_event()
        elif choice == '3':
            display_pending()
        elif choice == '4':
            event_name = input("Enter event name to cancel: ")
            cancel_event(event_name)
        elif choice == '5':
            print("Thank You!")
            break
        else:
            print("Invalid choice. Try again.")

menu()
