class Customer:
    def __init__(self, id, age, cart):
        self.id = id
        self.age = age
        self.cart = cart

class Queue:

    SENIOR_AGE = 62
    LEGAL_AGE = 18

    def __init__(self):
        self.queue = []

    def addQueue(self, customer):
        if(self.isLegalCustomer(customer)):
            if customer.age >=self.SENIOR_AGE: self.queue.insert(self.getLastSeniorQueueNumber(), customer)
            else: self.queue.append(customer)

    def getLastSeniorQueueNumber(self):
        queue_number = 0
        while queue_number < self.length() and self.queue[queue_number].age >= self.SENIOR_AGE: queue_number += 1
        return queue_number

    def isLegalCustomer(self, customer):
        if (customer.age < self.SENIOR_AGE and customer.age >= self.LEGAL_AGE): return True
        return self.isNotHavingProhibitedItems(customer)

    def isNotHavingProhibitedItems(self, customer):
        for item in customer.cart:
            if item in ["cigarette", "alcohol"]: return False
        return True

    def first(self):
        return self.queue[0]

    def last(self):
        return self.queue[-1]

    def length(self):
        return len(self.queue)