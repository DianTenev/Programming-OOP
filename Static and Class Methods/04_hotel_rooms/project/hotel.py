from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = [r for r in self.rooms if r.number == room_number][0]
            room.take_room(people)
        except IndexError:
            pass

    def free_room(self, room_number):
        try:
            room = [r for r in self.rooms if r.number == room_number][0]
            room.free_room()
        except IndexError:
            pass

    def status(self):
        free_rooms = ", ".join([str(x.number) for x in self.rooms if not x.is_taken])
        taken_rooms = ", ".join([str(x.number) for x in self.rooms if x.is_taken])
        return f"Hotel {self.name} has {sum([x.guests for x in self.rooms])} total guests\n" \
               f"Free rooms: {free_rooms}\n" \
               f"Taken rooms: {taken_rooms}\n"



