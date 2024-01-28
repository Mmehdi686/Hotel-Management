class Rooms:
    def __init__(self, room_id, room_type, status):
        self.room_id = room_id
        self.room_type = room_type
        self.status = status

    def set_room_status(self, new_status):
        self.status = new_status
        print(f"Room {self.room_id} status changed to {new_status}.")

    def schedule_room_maintenance(self, maintenance_type):
        print(f"Room {self.room_id} scheduled for {maintenance_type} maintenance.")

    def __str__(self):
        return f"Room ID: {self.room_id}, Type: {self.room_type}, Status: {self.status}"
