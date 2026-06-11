# Vacuum Cleaner Agent

# Initial state of rooms
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

# Vacuum starts in Room A
current_room = "A"

# Run until all rooms are clean
while True:

    print("\n-------------------------")
    print("Current Room :", current_room)
    print("Room Status  :", rooms[current_room])

    # Clean the room if it is dirty
    if rooms[current_room] == "Dirty":
        print("Action       : Cleaning the room...")
        rooms[current_room] = "Clean"
    else:
        print("Action       : Room is already clean.")

    # Check whether all rooms are clean
    if all(status == "Clean" for status in rooms.values()):
        print("\n All rooms are clean.")
        break

    # Move to the other room
    if current_room == "A":
        current_room = "B"
    else:
        current_room = "A"

# Display final status of all rooms
print("\n-------------------------")
print("Final Room Status:")
for room, status in rooms.items():
    print(f"Room {room}: {status}")




    # syntax: properties

'''
rooms = {"A": "Dirty", "B": "Dirty"}  # Dictionary

current_room = "A"                    # Variable Assignment

while True:                           # Infinite Loop

if condition:                         # If Statement
else:                                 # Else Statement

rooms[current_room]                   # Access Dictionary Value

rooms[current_room] = "Clean"         # Update Dictionary Value

all(status == "Clean" for status in rooms.values())  # all() Function

break                                 # Exit Loop

for room, status in rooms.items():    # For Loop

print()                               # Output Function

f"Room {room}: {status}"              # f-string

'''