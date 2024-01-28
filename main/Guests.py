from Person import Person

class Booking:
    def __init__(self, booking_id, guest_id, room_type, dates):
        self.booking_id = booking_id
        self.guest_id = guest_id
        self.room_type = room_type
        self.dates = dates

    def amend_dates(self, new_dates):
        self.dates = new_dates

class Feedback:
    def __init__(self, feedback_id, guest_id, feedback_text):
        self.feedback_id = feedback_id
        self.guest_id = guest_id
        self.feedback_text = feedback_text


class Guests(Person):
    def __init__(self, unique_id, name, contact_info):
        super().__init__(unique_id, name, contact_info)
        self.bookings = []
        self.feedback = []

    def request_room_booking(self, room_type, dates):
        booking_id = len(self.bookings) + 1
        new_booking = Booking(booking_id, self.unique_id, room_type, dates)
        self.bookings.append(new_booking)
        print(f"Booking {booking_id} created successfully.")
        return new_booking

    def amend_booking(self, booking_id, new_dates):
        booking = next((booking for booking in self.bookings if booking.booking_id == booking_id), None)
        if booking:
            booking.amend_dates(new_dates)
            print(f"Booking {booking_id} amended successfully.")
        else:
            print("Booking not found.")

    def cancel_booking(self, booking_id):
        booking_to_cancel = next((booking for booking in self.bookings if booking.booking_id == booking_id), None)
        if booking_to_cancel:
            self.bookings.remove(booking_to_cancel)
            print(f"Booking {booking_id} canceled successfully.")
        else:
            print("Booking not found.")

    def give_feedback(self, feedback_text):
        feedback_id = len(self.feedback) + 1
        new_feedback = Feedback(feedback_id, self.unique_id, feedback_text)
        self.feedback.append(new_feedback)
        print(f"Feedback {feedback_id} submitted successfully.")
        return new_feedback
