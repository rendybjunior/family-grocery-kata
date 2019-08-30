class Customer:
    def __init__(self, id, age, groceries):
        self.id = id
        self.age = age
        self.groceries = groceries # list of string

class Queue:
    def __init__(self):
        self.queue = []

    # Add new customer queue
    def add_queue(self, customer):
        is_banned_customer = self.is_banned(customer)

        if customer.age < 62:
            if customer.age < 18 and is_banned_customer:
                return
            self.queue.append(customer)

        if customer.age >= 62:
            if is_banned_customer:
                return

            sequence = 0
            while sequence < len(self.queue) and self.queue[sequence].age >= 62:
                sequence += 1
            # print(i)
            self.queue.insert(sequence, customer)

    #return true if groceries contains banned items of customer
    def is_banned(self, customer):
        banned_items = ["cigarette", "alcohol"]
        customer_age = customer.age

        for item in customer.groceries:
            if item in banned_items and (customer_age < 18 or customer_age >= 62):
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