
from Hotel import Hotel

def main():
    hotel = Hotel()

    while True:
        print("\nMain Menu:")
        print("1. Hotel Operations")
        print("2. Admin")
        print("3. Staff")
        print("4. Guests")
        print("5. Rooms")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            hotel.run_hotel_operations_menu()

        elif choice == "2":
            hotel.run_admin_menu()

        elif choice == "3":
            hotel.run_staff_menu()

        elif choice == "4":
            hotel.run_guests_menu()

        elif choice == "5":
            hotel.run_rooms_menu()

        elif choice == "6":
            print("Exiting Hotel Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
