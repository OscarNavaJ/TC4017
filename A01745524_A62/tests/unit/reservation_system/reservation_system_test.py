
"""
A01745524 - Oscar Nava Jiménez
MNA - TC4017 A6.2
"""
import coverage
import unittest
import reservation_system.reservation_system as ReservationSystem


class TestReservation(unittest.TestCase):
    """
        Tests reservation system with hotel and customer objects
    """
    def setUp(self):
        self.hotels = ReservationSystem.Hotels
        self.customers = ReservationSystem.Customers
        self.reservations = ReservationSystem.Reservation
        self.hotels.create_hotel("test_hotel")
        self.customers.create_customer("test_customer")

    def test_add_hotel(self):
        """
        Tests hotel creation
        """
        hotel_id = "test_hotel_create"
        self.assertNotIn(hotel_id,self.hotels.hotels)
        self.hotels.create_hotel(hotel_id)
        self.assertIn(hotel_id,self.hotels.hotels)

    def test_remove_hotel(self):
        """
        Tests hotel deletion
        """
        hotel_id = "test_hotel_delete"
        self.hotels.create_hotel(hotel_id)
        self.assertIn(hotel_id,self.hotels.hotels)
        self.hotels.delete_hotel(hotel_id)
        self.assertNotIn(hotel_id,self.hotels.hotels)

    def test_modify_hotel(self):
        """
        Tests hotel info modification
        """
        new_info = "testing hotel info modification"
        self.hotels.modify_hotel_info("test_hotel",new_info)
        self.assertEqual(self.hotels.hotels["test_hotel"].info, new_info)

    def test_add_customer(self):
        """
        Tests customer creation
        """
        customer_id = "test_customer_create"
        self.assertNotIn(customer_id,self.customers.customers)
        self.customers.create_customer(customer_id)
        self.assertIn(customer_id,self.customers.customers)

    def test_remove_customer(self):
        """
        Tests customer deletion
        """
        customer_id = "test_customer_delete"
        self.customers.create_customer(customer_id)
        self.assertIn(customer_id,self.customers.customers)
        self.customers.delete_customer(customer_id)
        self.assertNotIn(customer_id,self.customers.customers)

    def test_add_reservation(self):
        """
        Tests reservation creation
        """
        reservation = self.reservations("test_hotel", "test_customer")
        reservation.reserve_hotel_room()
        self.assertTrue(self.hotels.hotels["test_hotel"].reservations["test_customer"])

    def test_delete_reservation(self):
        """
        Tests reservation deletion
        """
        reservation = self.reservations("test_hotel", "test_customer")
        reservation.reserve_hotel_room()
        self.assertTrue(self.hotels.hotels["test_hotel"].reservations["test_customer"])
        reservation.cancel_hotel_reservation()
        self.assertFalse(self.hotels.hotels["test_hotel"].reservations["test_customer"])

class TestTC1Acceptation(unittest.TestCase):
    """
        Tests reservation system with hotel and customer objects for TC1
    """
    def test_TC1(self):
        """
        Tests TC1
        """
        ReservationSystem.main("tests/TC1/TC1.json")


if __name__ == '__main__':
    unittest.main()
