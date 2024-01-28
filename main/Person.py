class Person:
    def __init__(self, unique_id, name, contact_info):
        self.unique_id = unique_id
        self.name = name
        self.contact_info = contact_info

    def update_contact_details(self, new_contact_info):
        self.contact_info = new_contact_info

    def __str__(self):
        return f"ID: {self.unique_id}, Name: {self.name}, Contact Info: {self.contact_info}"
