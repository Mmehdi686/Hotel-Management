from Person import Person
from Staff import Staff

class Admin(Person):
    def __init__(self, unique_id, name, contact_info):
        super().__init__(unique_id, name, contact_info)
        self.staff_members = []

    def create_staff_account(self, staff_details):
        try:
            new_staff = Staff(unique_id=len(self.staff_members) + 1,
                              name=staff_details['name'],
                              contact_info=staff_details['contact_info'],
                              role=staff_details['role'])
            self.staff_members.append(new_staff)
            print(f"Staff member {new_staff.name} created successfully.")
            return new_staff
        except Exception as e:
            print(f"Error creating staff account: {e}")

    def remove_staff_member(self, staff_id):
        try:
            staff_to_remove = next((staff for staff in self.staff_members if staff.unique_id == staff_id), None)
            if staff_to_remove:
                self.staff_members.remove(staff_to_remove)
                print(f"Staff member {staff_id} removed successfully.")
            else:
                print("Staff member not found.")
        except Exception as e:
            print(f"Error removing staff member: {e}")

    def update_staff_role(self, staff_id, new_role):
        staff = next((staff for staff in self.staff_members if staff.unique_id == staff_id), None)
        if staff:
            staff.update_role(new_role)
            print(f"Staff member {staff_id}'s role updated to {new_role} successfully.")
        else:
            print("Staff member not found.")

    def generate_payroll_report(self):
        print("Staff Payroll Report:")
        for staff in self.staff_members:
            print(f"Staff ID: {staff.unique_id}, Name: {staff.name}, Role: {staff.role}, Salary: {staff.calculate_salary()}")

    def view_staff_salaries(self):
        print("Staff Salaries:")
        for staff in self.staff_members:
            print(f"Staff ID: {staff.unique_id}, Name: {staff.name}, Salary: {staff.calculate_salary()}")