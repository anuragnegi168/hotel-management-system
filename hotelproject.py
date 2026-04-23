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

def book_room():
    print("-----Room Booking-----")
    try:
        room = int(input("Enter the room you want to book : "))
    except:
        print("Invalid input")
        return

    for r in rooms:
        if r["Room No"] == room:
            if r["Available"] == True:
                r["Customer Name"] = input("Enter the name of customer : ")
                r["Days"] = int(input("Enter the days customer want to stay : "))
                r["Phone Number"] = input("Enter the customer phone number : ")
                r["Available"] = False
                print(f"Room {room} booked successfully for {r['Customer Name']}")
                break
            else:
                print("room not available:")
                break
    else:
        print("Room not found")


def checkout_room():
    print("-----Checkout Room-----")
    try:
        room = int(input("Enter the room no : "))
    except:
        print("Invalid input")
        return
    
    for r in rooms:
        if r["Room No"] == room:
            if not r["Available"]:
                r["Customer Name"] = ""
                r["Days"] = 0
                r["Phone Number"] = ""
                r["Available"] = True
                print("Room Checkout successfully")
                break
            else:
                print("Room is already empty")
                break
    else:
        print("Room not found")
        
def search_room():
    print("-----search Rooms-----")
    try:
        room = int(input("Enter the room no : "))
    except:
        print("Invalid input")
        return
    
    for r in rooms:
        if r["Room No"] == room:
            print(f"Room: {r['Room No']}, Type: {r['Room Type']}, Price: {r['Price']}, Available: {r['Available']}")
            break
    else:
        print("Room not found")
        

def update_room():
    print("-----Update Rooms-----")
    try:
        room = int(input("Enter the room no you want to update : "))
    except:
        print("Invalid input")
        return
    
    for r in rooms:
        if r["Room No"] == room:
            while True:
                r_type = input("Enter the room Type (Ac, Non-AC, Deluxe) : ").strip()
                if r_type.lower() in [t.lower() for t in room_type]:
                    for t in room_type:
                        if t.lower() == r_type.lower():
                            r_type = t
                            r["Room Type"] = r_type
                            break
                    break
                else:
                    print("Invalid input")
            try:
                r["Price"] = int(input("Enter the room price : "))
                print("Room updated successfully")
                break
            except:
                print("Invalid input,try again")
    else:
        print("Room not found")

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
    elif choice == 3:
        book_room()
    elif choice == 4:
        checkout_room()
    elif choice == 5:
        search_room()
    elif choice == 6:
        update_room()
    elif choice == 12:
        break
    else:
        print("Invalid Input")
