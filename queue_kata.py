from typing import List

class Customer:
    def __init__(self, id: str, age: int, items: List[str]):
        self.id: str = id
        self.age: int = age
        self.items: List[str] = items

class FamilyGroceryQueue:
    PROHIBITED_ITEMS: List[str] = ["cigarette", "alcohol"]
    SENIOR_AGE = 62

    def __init__(self):
        self.customers: List[str] = []

    def add_customer(self, new_customer: Customer) -> None:
        if not self.check_seniority(new_customer):
            if new_customer.age < 18:
                if self.check_non_prohibited_items(new_customer):
                    return
            self.customers.append(new_customer)
        if self.check_seniority(new_customer):
            if self.check_non_prohibited_items(new_customer):
                return
            customer_order_based_on_age = 0
            while (
                    customer_order_based_on_age < len(self.customers)
                    and self.check_seniority(self.customers[customer_order_based_on_age])
                ):
                customer_order_based_on_age += 1

            self.customers.insert(customer_order_based_on_age, new_customer)

    def first(self) -> Customer:
        return self.customers[0]

    def check_non_prohibited_items(self, customer) -> bool:
        for item in customer.items:
            if item in FamilyGroceryQueue.PROHIBITED_ITEMS:
                return True
        return False

    def check_seniority(self, customer):
        return customer.age >= FamilyGroceryQueue.SENIOR_AGE

    def last(self) -> Customer:
        return self.customers[-1]

    def length(self) -> int:
        return len(self.customers)
