from Person import Person

class Staff(Person):
    def __init__(self, unique_id, name, contact_info, role):
        super().__init__(unique_id, name, contact_info)
        self.role = role

    def update_role(self, new_role):
        self.role = new_role

    def calculate_salary(self):
        return 5000

    def book_guest(self, guest_id, room_id):
        try:
            guest = next((guest for guest in self.guests if guest.unique_id == guest_id), None)
            room = next((room for room in self.rooms if room.room_id == room_id), None)

            if guest and room and room.status == "Vacant":
                room.status = "Occupied"
                print(f"Guest {guest.name} booked successfully into Room {room.room_id}.")
            else:
                print("Booking failed. Please check guest and room details.")
        except Exception as e:
            print(f"Error booking guest: {e}")

    def check_out_guest(self, guest_id):
        try:
            guest = next((guest for guest in self.guests if guest.unique_id == guest_id), None)

            if guest:
                guest_room = next((room for room in self.rooms if room.room_id == guest.room_id), None)
                if guest_room:
                    guest_room.status = "Vacant"
                    print(f"Guest {guest.name} checked out successfully from Room {guest_room.room_id}.")
                else:
                    print("Room not found for the guest.")
            else:
                print("Guest not found.")
        except Exception as e:
            print(f"Error checking out guest: {e}")

    def mark_room_cleaned(self, room_id):
        room = next((room for room in self.rooms if room.room_id == room_id), None)

        if room:
            room.status = "Vacant"
            print(f"Room {room_id} marked as cleaned and vacant.")
        else:
            print("Room not found.")

    def request_cleaning_supplies(self):
        print("Cleaning supplies requested.")

    def report_repair_done(self, room_id):
        room = next((room for room in self.rooms if room.room_id == room_id), None)

        if room:
            print(f"Repair in Room {room_id} is marked as done.")
        else:
            print("Room not found.")

    def order_repair_materials(self, material_list):
        print(f"Repair materials ordered: {material_list}")
        
class Maintenance(Staff):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info, role="Maintenance")


class Housekeeping(Staff):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info, role="Housekeeping")


class Receptionist(Staff):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info, role="Receptionist")
