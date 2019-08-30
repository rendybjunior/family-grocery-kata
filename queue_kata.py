class Customer:
    def __init__(self, id, age, groceries):
        self.id = id
        self.age = age
        self.groceries = groceries # list of string

class Queue:
    def __init__(self):
        self.queue = []
        self.MINOR_AGE_LIMIT = 18
        self.SENIOR_AGE_LIMIT = 62

    # Add new customer queue
    def add_queue(self, customer):
        is_banned_customer = self.is_banned(customer)

        if customer.age < self.SENIOR_AGE_LIMIT:
            if customer.age < self.MINOR_AGE_LIMIT and is_banned_customer:
                return
            self.queue.append(customer)

        if customer.age >= self.SENIOR_AGE_LIMIT:
            if is_banned_customer:
                return

            sequence = 0
            while sequence < len(self.queue) and self.queue[sequence].age >= self.SENIOR_AGE_LIMIT:
                sequence += 1
            # print(i)
            self.queue.insert(sequence, customer)

    #return true if groceries contains banned items of customer
    def is_banned(self, customer):
        banned_items = ["cigarette", "alcohol"]
        customer_age = customer.age

        for item in customer.groceries:
            if item in banned_items and (customer_age < self.MINOR_AGE_LIMIT or customer_age >= self.SENIOR_AGE_LIMIT):
                return True
        return False

    # Return first item
    def first(self):
        return self.queue[0]

    # Return last item
    def last(self):
        return self.queue[-1]

    # Return queue length
    def length(self):
        return len(self.queue)