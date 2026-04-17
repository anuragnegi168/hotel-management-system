rooms = [{"Room No":100,"Room Type":"Non-AC","Price":1000,"Available":True,"Customer Name":"","Days":0,"Phone Number":""}]
room_type = ("Ac","Non-AC","Deluxe")


def add_room():
    print("add new rooms in system")
    
    while True:
        room = int(input("Enter The room no : "))
        if any (r["Room No"] == room for r in rooms):
            print("Room Already exist")
        else:
            break

    while True:
        r_type = input("Enter the room Type (Ac, Non-AC, Deluxe) : ").strip()
        if r_type.lower() in [r.lower() for r in room_type]:
            for r in room_type:
                if r.lower() == r_type.lower():
                    r_type = r
                    break
            break
        else:
            print("Invalid input")
    price = int(input("Enter the price per day : "))
    available = True

    add = {"Room No.":room,"Room Type":room_type,"Price per day":price,"Availability":available,
           "Customer Name":"","Days Stayed":0,"Phone number":""}
    
    rooms.append(add)
    print("Room added successfully")


def view_rooms():
    for r in rooms:
        print(f"Room: {["Room No"]} , Type: {["Room Type"]} , Price: {["Price"]} , Available: {["Available"]}")

while True:
    print("\n----------Hotel Management System----------")
    print("""\n1. Add Room
2. View All Rooms
3. Book Room
4. Check-Out Room
5. Search Room
6. Update Room
7. Delete Room
8. Show Available Rooms
9. Show Booked Rooms
10. Generate Bill
11. Hotel Summary
12. Exit """)
    choice = int(input("Enter the menu number : "))

    if choice == 1:
        add_room()
    elif choice == 2:
        view_rooms()
    elif choice == 12:
        break
    else:
        print("Invalid Input")