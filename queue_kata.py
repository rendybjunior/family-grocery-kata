from typing import List

class Customer:
    def __init__(self, id: str, age: int, items: List[str]):
        self.id: str = id
        self.age: int = age
        self.items: List[str] = items

    def is_senior(self) -> bool:
        return self.age >= 62

class Queue:
    def __init__(self):
        self.customers: List[str] = []
        self.prohibited_items: List[str] = ["cigarette", "alcohol"]

    def add_customer(self, new_customer: Customer) -> None:
        if not new_customer.is_senior():
            if new_customer.age < 18:
                if self.has_non_prohibited_items(new_customer):
                    return
            self.customers.append(new_customer)
        if new_customer.is_senior():
            if self.has_non_prohibited_items(new_customer):
                return
            customer_order_based_on_age = 0
            while customer_order_based_on_age < len(self.customers) and self.customers[customer_order_based_on_age].is_senior():
                customer_order_based_on_age += 1

            self.customers.insert(customer_order_based_on_age, new_customer)

    # Return first item
    def first(self) -> Customer:
        return self.customers[0]

    def has_non_prohibited_items(self, customer) -> bool:
        for item in customer.items:
            if item in self.prohibited_items:
                return True
        return False

    # Return last item
    def last(self) -> Customer:
        return self.customers[-1]

    # Return queue length
    def length(self) -> int:
        return len(self.customers)
