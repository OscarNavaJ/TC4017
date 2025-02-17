
"""
A01745524 - Oscar Nava Jiménez
MNA - TC4017 A6.2
"""
import argparse
import time
import json


class Hotel:
    """
    Hotel object
    """
    def __init__(self, hotel_id):
        self.id = hotel_id
        self.info = None
        self.reservations = {}

    def __repr__(self):
        return f"Hotel {self.id} {self.info}"

    def display_hotel_info(self):
        """
        Shows customer info
        :return:
        """
        return self.info


class Hotels:
    """
    Aggregation class for hotels
    """

    hotels = {}

    @staticmethod
    def create_hotel(uuid):
        """
        Creates instance of hotel, appends it to hotel list
        and returns a unique id
        :return:
        """
        hotel_id = uuid
        Hotels.hotels.update({hotel_id: Hotel(hotel_id)})

    @staticmethod
    def delete_hotel(hotel_id):
        """
        Removes hotel by unique identifier
        :param hotel_id: unique identifier
        :return:
        """
        Hotels.hotels.pop(hotel_id)

    @staticmethod
    def display_hotel_info(hotel_id):
        """
        Shows hotel information by unique identifier
        :param hotel_id: unique identifier
        :return:
        """
        if hotel_id in Hotels.hotels:
            print(Hotels.hotels[hotel_id].info)
        else:
            raise ValueError("ID not found")

    @staticmethod
    def modify_hotel_info(hotel_id, new_info):
        """
        Modifies hotel information by unique identifier
        :param hotel_id: unique identifier
        :param new_info: modified info to be updated
        :return:
        """
        if hotel_id in Hotels.hotels:
            Hotels.hotels[hotel_id].info = new_info
        else:
            raise ValueError("ID not found")

    @staticmethod
    def reserve_hotel_room(hotel_id, customer_id):
        """
       Creates a reservation for a given customer
       :param hotel_id: unique identifier
       :param customer_id: customer identifier
       :return:
       """
        Hotels.hotels[hotel_id].reservations[customer_id] = True

    @staticmethod
    def cancel_hotel_reservation(hotel_id, customer_id):
        """
       Cancels a reservation for a given customer
       :param hotel_id: unique identifier
       :param customer_id: customer identifier
       :return:
       """
        Hotels.hotels[hotel_id].reservations[customer_id] = False


class Customer:
    """
    Customer object
    """
    def __init__(self, customer_id):
        self.id = customer_id
        self.info = None

    def __repr__(self):
        return f"Customer {self.id} {self.info}"

    def display_customer_info(self):
        """
        Shows customer info
        :return:
        """
        return self.info


class Customers:
    """
    Aggregation class for customers
    """
    customers = {}

    @staticmethod
    def create_customer(uuid):
        """
        Creates customer instance and adds it to class aggregation
        :return:
        """
        customer_id = uuid
        Customers.customers.update({customer_id: Customer(customer_id)})

    @staticmethod
    def delete_customer(customer_id):
        """
        Removes customer by unique identifier
        :param customer_id: unique identifier
        :return:
        """
        Customers.customers.pop(customer_id)

    @staticmethod
    def display_customer_info(customer_id):
        """
        Shows customer information by unique identifier
        :param customer_id: unique identifier
        :return:
        """
        if customer_id in Customers.customers:
            print(Customers.customers[customer_id].info)
        else:
            raise ValueError("ID not found")

    @staticmethod
    def modify_customer_info(customer_id, new_info):
        """
        Modifies customer information by unique identifier
        :param customer_id: unique identifier
        :param new_info: modified info to be updated
        :return:
        """
        if customer_id in Customers.customers:
            Customers.customers[customer_id].info = new_info
        else:
            raise ValueError("ID not found")


class Reservation:
    """
    reservation object
    """
    def __init__(self, hotel_id, customer_id):
        self.hotel_id = hotel_id
        self.customer_id = customer_id

    def reserve_hotel_room(self):
        """
        Carries out hotel reservation by hotel id and customer id
        :return:
        """
        Hotels.reserve_hotel_room(self.hotel_id, self.customer_id)

    def cancel_hotel_reservation(self):
        """
        Cancels hotel reservation by hotel id and customer id
        :return:
        """
        Hotels.cancel_hotel_reservation(self.hotel_id, self.customer_id)


def main(reservation_path: str):
    """
    :param reservation_path:str File path of reservations to be received
    :return:
    """
    start_time = time.perf_counter()
    with open(reservation_path, "r+", encoding="UTF-8") as f:
        reservation_data = json.load(f)

    for el in reservation_data:
        if el["type"] == "hotel" and el["action"] == "creation":
            Hotels.create_hotel(el["hotel_id"])
            Hotels.modify_hotel_info(el["hotel_id"], el["hotel_info"])
            Hotels.display_hotel_info(el["hotel_id"])
        elif el["type"] == "hotel" and el["action"] == "deletion":
            Hotels.delete_hotel(el["hotel_id"])
        elif el["type"] == "customer" and el["action"] == "creation":
            Customers.create_customer(el["customer_id"])
            Customers.modify_customer_info(el["customer_id"],
                                           el["customer_info"])
            Customers.display_customer_info(el["customer_id"])
        elif el["type"] == "customer" and el["action"] == "deletion":
            Customers.delete_customer(el["customer_id"])
        elif el["type"] == "customer" and el["action"] == "reservation":
            reservation = Reservation(el["hotel_id"], el["customer_id"])
            reservation.reserve_hotel_room()
        elif el["type"] == "customer" and el["action"] == "cancel_reservation":
            reservation = Reservation(el["hotel_id"], el["customer_id"])
            reservation.cancel_hotel_reservation()

    end_time = time.perf_counter()
    exec_time = end_time-start_time
    with open("ReservationResults.txt", "w", encoding="UTF-8") as f:
        f.write(f"EXECUTION TIME: {exec_time} s\n")
    print(f"EXECUTION TIME: {exec_time} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("reservation_file", type=str)
    args = parser.parse_args()
    reservation_file = args.reservation_file
    main(reservation_file)
