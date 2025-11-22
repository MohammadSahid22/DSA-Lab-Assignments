import random

class Flight:
    def __init__(self, flight_no, source, destination, date, time):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.date = date
        self.time = time
        self.fares = {"business": 5000, "premium": 3000, "economy": 1500}
        self.seats = {"business": 5, "premium": 10, "economy": 30}
        self.passengers = []

    def generate_pnr(self):
        return "PNR" + str(random.randint(10000, 99999))

    def book_ticket(self, name, seat_class):
        if self.seats[seat_class] > 0:
            self.seats[seat_class] -= 1
            pnr = self.generate_pnr()
            ticket = {
                "pnr": pnr,
                "name": name,
                "class": seat_class,
                "fare": self.fares[seat_class],
                "seat_no": f"{seat_class[0].upper()}{self.seats[seat_class]}"
            }
            self.passengers.append(ticket)
            print(f"\n Ticket booked successfully!")
            print(f"PNR: {pnr}, Seat No: {ticket['seat_no']}, Fare: Rs:{ticket['fare']}\n")
        else:
            print(f"\n {seat_class.capitalize()} class is full! Booking failed.\n")

    def cancel_ticket(self, pnr):
        for passenger in self.passengers:
            if passenger["pnr"] == pnr:
                self.passengers.remove(passenger)
                seat_class = passenger["class"]
                self.seats[seat_class] += 1
                print(f"\n Ticket with PNR {pnr} cancelled. Refund: Rs:{passenger['fare']}\n")
                return
        print(f"\n PNR {pnr} not found!\n")

    def display_flight(self):
        print(f"Flight {self.flight_no}: {self.source} → {self.destination} on {self.date} at {self.time}")
        print("Available Seats:", self.seats)

    def display_passengers(self):
        print(f"\n Passenger List for Flight {self.flight_no}")
        if not self.passengers:
            print("No passengers yet.")
            return
        sorted_passengers = sorted(self.passengers, key=lambda x: x["name"].lower())
        for p in sorted_passengers:
            print(p)
        print()


def quick_sort(flights_list, key):
    if len(flights_list) <= 1:
        return flights_list
    pivot = getattr(flights_list[len(flights_list)//2], key)
    left = [f for f in flights_list if getattr(f, key) < pivot]
    middle = [f for f in flights_list if getattr(f, key) == pivot]
    right = [f for f in flights_list if getattr(f, key) > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)


def binary_search(flights_list, flight_no):
    low = 0
    high = len(flights_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if flights_list[mid].flight_no == flight_no:
            return flights_list[mid]
        elif flights_list[mid].flight_no < flight_no:
            low = mid + 1
        else:
            high = mid - 1
    return None


def display_sorted_flights(flights, sort_by="flight_no"):
    if not flights:
        print("\n No flights available!\n")
        return
    flights_list = list(flights.values())
    sorted_list = quick_sort(flights_list, sort_by)
    for f in sorted_list:
        f.display_flight()


def search_flight(flights, source, destination):
    found = False
    for f in flights.values():
        if f.source.lower() == source.lower() and f.destination.lower() == destination.lower():
            f.display_flight()
            found = True
    if not found:
        print("\n No flights found for this route!\n")


flights = {
    101: Flight(101, "Pune", "Delhi", "2025-10-01", "10:00"),
    102: Flight(102, "Mumbai", "Bangalore", "2025-10-02", "14:30"),
    103: Flight(103, "Delhi", "Kolkata", "2025-10-03", "09:15"),
    104: Flight(104, "Bangalore", "Chennai", "2025-10-03", "11:45"),
    105: Flight(105, "Hyderabad", "Pune", "2025-10-04", "07:50"),
}

while True:
    print("\n---Flight Reservation System---")
    print("1. Add Flight")
    print("2. Display Flights (Quick Sort)")
    print("3. Search Flight by Source/Destination")
    print("4. Search Flight by Number (Binary Search)")
    print("5. Book Ticket")
    print("6. Cancel Ticket")
    print("7. Display Passengers")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        fno = int(input("Enter flight number: "))
        src = input("Enter source: ")
        dst = input("Enter destination: ")
        date = input("Enter date (YYYY-MM-DD): ")
        time = input("Enter time (HH:MM): ")
        flights[fno] = Flight(fno, src, dst, date, time)
        print("\n Flight added successfully!\n")

    elif choice == "2":
        print("\nSort Flights By:")
        print("1. Flight Number")
        print("2. Source")
        print("3. Destination")
        print("4. Date")
        opt = input("Enter choice: ")
        sort_key = {"1": "flight_no", "2": "source", "3": "destination", "4": "date"}.get(opt, "flight_no")
        display_sorted_flights(flights, sort_key)

    elif choice == "3":
        src = input("Enter source: ")
        dst = input("Enter destination: ")
        search_flight(flights, src, dst)

    elif choice == "4":
        flight_no = int(input("Enter flight number to search: "))
        sorted_list = quick_sort(list(flights.values()), "flight_no")
        found_flight = binary_search(sorted_list, flight_no)
        if found_flight:
            print("\n Flight found:\n")
            found_flight.display_flight()
        else:
            print("\n Flight not found!\n")

    elif choice == "5":
        fno = int(input("Enter flight number: "))
        if fno in flights:
            name = input("Enter passenger name: ")
            print("Choose Class: 1. Business 2. Premium 3. Economy")
            cls_choice = input("Enter choice: ")
            seat_class = "business" if cls_choice == "1" else "premium" if cls_choice == "2" else "economy"
            flights[fno].book_ticket(name, seat_class)
        else:
            print("\n Flight not found!\n")

    elif choice == "6":
        fno = int(input("Enter flight number: "))
        pnr = input("Enter PNR to cancel: ")
        if fno in flights:
            flights[fno].cancel_ticket(pnr)
        else:
            print("\n Flight not found!\n")

    elif choice == "7":
        fno = int(input("Enter flight number: "))
        if fno in flights:
            flights[fno].display_passengers()
        else:
            print("\n Flight not found!\n")

    elif choice == "8":
        print("\n Thank you for using Flight Reservation System!\n")
        break

    else:
        print("\n Invalid choice!!!")
