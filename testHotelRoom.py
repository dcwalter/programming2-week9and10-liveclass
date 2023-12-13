import unittest
from HotelRoom import HotelRoom

class Test (unittest.TestCase):
    def test_init(self):
        room = HotelRoom(100, 2, 100.00)
        self.assertEqual(room.room_number, 100)
        self.assertEqual(room.capacity, 2)
        self.assertEqual(room.rate, 100.00)
        self.assertEqual(room.occupants, [])
        self.assertEqual(room.number_of_nights, 0)
        self.assertEqual(room.total_charge, 0.00)

    def test_check_in(self):
        room = HotelRoom(100, 2, 100.00)
        room.check_in("John Doe")
        self.assertEqual(room.occupants, ["John Doe"])

    def test_check_out(self):
        room = HotelRoom(100, 2, 100.00)
        room.occupants = ["John Doe"]
        room.check_out()
        self.assertEqual(room.occupants, [])

    def test_add_nights(self):
        room = HotelRoom(100, 2, 100.00)
        room.add_nights(3)
        self.assertEqual(room.number_of_nights, 3)

    def test_total_charge(self):
        room = HotelRoom(100, 2, 100.00)
        room.add_nights(3)
        self.assertEqual(room.total_charge, 300.00)

if __name__ == '__main__':
    unittest.main()