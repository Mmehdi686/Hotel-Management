from Admin import Admin
from Staff import Maintenance, Housekeeping, Receptionist, Staff
from Guests import Guests
from Rooms import Rooms

class Hotel:
    def __init__(self):
        self.rooms = [] 
        self.guests = []  
        self.staff = []   

    def list_available_rooms(self, room_type):
        try:
            available_rooms = [room for room in self.rooms if room.room_type == room_type and room.status == "Vacant"]
            if available_rooms:
                print(f"Available {room_type} rooms:")
                for room in available_rooms:
                    print(room)
            else:
                print(f"No available {room_type} rooms.")
        except Exception as e:
            print(f"Error listing available rooms: {e}")

    def get_guest_details(self, guest_id):
        try:
            guest = next((guest for guest in self.guests if guest.unique_id == guest_id), None)
            if guest:
                print("Guest Details:")
                print(guest)
            else:
                print("Guest not found.")
        except Exception as e:
            print(f"Error getting guest details: {e}")

    def run_admin_menu(self):
        admin_password = input("Enter admin password: ") 
        if admin_password == "123": 
            while True:
                print("\nAdmin Menu:")
                print("1. Create Staff Account")
                print("2. Remove Staff Member")
                print("3. Update Staff Role")
                print("4. View Staff Salaries")
                print("5. Generate Payroll Report")
                print("6. Back to Main Menu")

                admin_choice = input("Enter your choice (1-6): ")

                if admin_choice == "1":
                    staff_details = {
                        "name": input("Enter staff name: "),
                        "contact_info": input("Enter staff contact info: "),
                        "role": input("Enter staff role: ")
                    }
                    self.admin.create_staff_account(staff_details)

                elif admin_choice == "2":
                    staff_id = int(input("Enter staff ID to remove: "))
                    self.admin.remove_staff_member(staff_id)

                elif admin_choice == "3":
                    staff_id = int(input("Enter staff ID to update role: "))
                    new_role = input("Enter new role: ")
                    self.admin.update_staff_role(staff_id, new_role)

                elif admin_choice == "4":
                    self.admin.view_staff_salaries()

                elif admin_choice == "5":
                    self.admin.generate_payroll_report()

                elif admin_choice == "6":
                    print("Returning to Main Menu.")
                    break

                else:
                    print("Invalid choice. Please enter a valid option.")
        else:
            print("Incorrect admin password. Access denied.")

    def get_staff_role(self, staff_id):
        staff = next((staff for staff in self.staff if staff.unique_id == staff_id), None)
        if staff:
            return staff.role
        else:
            return "Staff not found"


    def run_staff_menu(self):
        staff_id = int(input("Enter staff ID: ")) 
        staff = next((staff for staff in self.staff if staff.unique_id == staff_id), None)

        if staff:
            while True:
                print("\nStaff Menu:")
                print("1. Book Guest (Receptionist)")
                print("2. Check Out Guest (Receptionist)")
                print("3. Mark Room Cleaned (Housekeeping)")
                print("4. Request Cleaning Supplies (Housekeeping)")
                print("5. Report Repair Done (Maintenance)")
                print("6. Order Repair Materials (Maintenance)")
                print("7. Back to Main Menu")

                staff_choice = input("Enter your choice (1-7): ")

                if staff_choice == "1" and isinstance(staff, Receptionist):
                    guest_id = int(input("Enter guest ID: "))
                    room_id = int(input("Enter room ID: "))
                    staff.book_guest(guest_id, room_id)

                elif staff_choice == "2" and isinstance(staff, Receptionist):
                    guest_id = int(input("Enter guest ID: "))
                    staff.check_out_guest(guest_id)

                elif staff_choice == "3" and isinstance(staff, Housekeeping):
                    room_id = int(input("Enter room ID: "))
                    staff.mark_room_cleaned(room_id)

                elif staff_choice == "4" and isinstance(staff, Housekeeping):
                    staff.request_cleaning_supplies()

                elif staff_choice == "5" and isinstance(staff, Maintenance):
                    room_id = int(input("Enter room ID: "))
                    staff.report_repair_done(room_id)

                elif staff_choice == "6" and isinstance(staff, Maintenance):
                    material_list = input("Enter a list of repair materials: ")
                    staff.order_repair_materials(material_list)

                elif staff_choice == "7":
                    print("Returning to Main Menu.")
                    break

                else:
                    print("Invalid choice. Please enter a valid option.")
        else:
            print("Staff not found. Access denied.")

    def run_guests_menu(self):
        guest_id = int(input("Enter guest ID: ")) 
        guest = next((guest for guest in self.guests if guest.unique_id == guest_id), None)

        if guest:
            while True:
                print("\nGuests Menu:")
                print("1. Request Room Booking")
                print("2. Edit Booking")
                print("3. Cancel Booking")
                print("4. Give Feedback")
                print("5. Back to Main Menu")

                guest_choice = input("Enter your choice (1-5): ")

                if guest_choice == "1":
                    room_type = input("Enter room type: ")
                    dates = input("Enter booking dates: ")
                    guest.request_room_booking(room_type, dates)

                elif guest_choice == "2":
                    booking_id = int(input("Enter booking ID to amend: "))
                    new_dates = input("Enter new booking dates: ")
                    guest.amend_booking(booking_id, new_dates)

                elif guest_choice == "3":
                    booking_id = int(input("Enter booking ID to cancel: "))
                    guest.cancel_booking(booking_id)

                elif guest_choice == "4":
                    feedback_text = input("Enter your feedback: ")
                    guest.give_feedback(feedback_text)

                elif guest_choice == "5":
                    print("Returning to Main Menu.")
                    break

                else:
                    print("Invalid choice. Please enter a valid option.")
        else:
            print("Guest not found. Access denied.")

    def run_rooms_menu(self):
        print("\nRooms Menu:")
        print("1. Set Room Status")
        print("2. Schedule Room Maintenance")
        print("3. Back to Main Menu")

        rooms_choice = input("Enter your choice (1-4): ")

        if rooms_choice == "1":
            room_id = int(input("Enter room ID: "))
            new_status = input("Enter new room status: ")
            self.set_room_status(room_id, new_status)

        elif rooms_choice == "2":
            room_id = int(input("Enter room ID: "))
            maintenance_type = input("Enter maintenance type: ")
            self.schedule_room_maintenance(room_id, maintenance_type)

        elif rooms_choice == "3":
            print("Returning to Main Menu.")

        else:
            print("Invalid choice. Please enter a valid option.")

    def run_hotel_operations_menu(self):
        print("\nHotel Operations Menu:")
        print("1. List available rooms")
        print("2. Get guest details")
        print("3. Back to Hotel Menu")

        hotel_operations_choice = input("Enter your choice (1-4): ")

        if hotel_operations_choice == "1":
            room_type = input("Enter room type to list available rooms: ")
            self.list_available_rooms(room_type)

        elif hotel_operations_choice == "2":
            guest_id = input("Enter guest ID to get details: ")
            self.get_guest_details(guest_id)

        elif hotel_operations_choice == "3":
            print("Returning to Hotel Menu.")

        else:
            print("Invalid choice. Please enter a valid option.")


    


