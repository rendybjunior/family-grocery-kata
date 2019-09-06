class Customer:
    def __init__(self, id, age, cart):
        self.id = id
        self.age = age
        self.cart = cart # list of string

class Queue:
    def __init__(self):
        self.queue = []
        self.SENIOR_AGE=62
        self.LEGAL_AGE=18

    # Add new item
    def add_queue(self, customer):
        if(not self.isNotLegalCustomer(customer)):
            if customer.age >=self.SENIOR_AGE:
                self.queue.insert(self.getLastSeniorQueueNumber(), customer)
            else:
                self.queue.append(customer)

    # Return queue number after the last senior age
    def getLastSeniorQueueNumber(self):
        queue_number = 0
        while queue_number < self.length() and self.queue[queue_number].age >= self.SENIOR_AGE:
            queue_number += 1
        return queue_number

    # Return confirmation whether the customer met the requirements for having legal items
    def isNotLegalCustomer(self, customer):
        if (customer.age >= self.SENIOR_AGE or customer.age < self.LEGAL_AGE):
            return self.isHavingProhibitedItems(customer)
        return False

    # Return confirmation for having prohibited items
    def isHavingProhibitedItems(self, customer):
        for item in customer.cart:
            if item in ["cigarette", "alcohol"]:
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