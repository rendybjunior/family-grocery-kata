class Customer:
    def __init__(self, id, age, items):
        self.id = id
        self.age = age
        self.items = items # list of string

class Queue:
    def __init__(self):
        self.queue = []
        self.prohibited_items = ["cigarette", "alcohol"]
        self.minimum_age_threshold = 0
        self.underage_age_threshold = 18
        self.senior_age_threshold = 62

    # customer check function
    def check_customer_age_validity(self, customer):
        if customer.age < self.minimum_age_threshold:
            return False
        else:
            return True

    def check_underage_customer(self, customer):
        if customer.age < self.underage_age_threshold:
            return True
        else:
            return False

    def check_senior_customer(self, customer):
        if customer.age >= self.senior_age_threshold:
            return True
        else:
            return False

    def check_prohibited_items(self, customer):
        for item in customer.items:
            if item in self.prohibited_items:
                return True
        return False

    # Add new customer
    def add_customer(self, customer):

        if self.check_customer_age_validity(customer):

            if not self.check_senior_customer(customer):
                if self.check_underage_customer(customer):
                    if self.check_prohibited_items(customer):
                        return
                self.queue.append(customer)

            if self.check_senior_customer(customer):
                if self.check_prohibited_items(customer):
                    return

                sequence = 0

                while sequence < len(self.queue) and self.queue[sequence].age >= self.senior_age_threshold:
                    sequence += 1

                self.queue.insert(sequence, customer)

    # Return first item
    def first(self):
        return self.queue[0]

    # Return last item
    def last(self):
        return self.queue[-1]

    # Return queue length
    def length(self):
        return len(self.queue)
