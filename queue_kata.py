class Customer:
    def __init__(self, id, age, groceries):
        self.id = id
        self.age = age
        self.groceries = groceries

class Queue:
    def __init__(self):
        self.queueLine = []
        self.prohibitedGroceries = ["cigarette", "alcohol"]
        self.seniorAge = 62
        self.adultAge = 18
        self.lastSeniorQueueIndex = 0

    # Add new customer to queue line
    def add_to_queue(self, customer):

        def _is_senior(age):
            return True if age >= self.seniorAge else False
        
        def _is_adult(age):
            return True if age >= self.adultAge else False

        def _remove_prohobited_grocery(groceries):
            for grocery in groceries:
                if grocery in self.prohibitedGroceries:
                    groceries.remove(grocery)

        if not _is_senior(customer.age):
            if not _is_adult(customer.age):
                _remove_prohobited_grocery(customer.groceries)
            if len(customer.groceries) is not 0:
                self.queueLine.append(customer)
        if _is_senior(customer.age):
            _remove_prohobited_grocery(customer.groceries)
            if len(customer.groceries) is not 0:
                while self.lastSeniorQueueIndex < len(self.queueLine) and _is_senior(self.queueLine[self.lastSeniorQueueIndex].age):
                    self.lastSeniorQueueIndex += 1
                self.queueLine.insert(self.lastSeniorQueueIndex, customer)

    # Return first queue
    def get_first_queue(self):
        return self.queueLine[0]

    # Return last queue
    def get_last_queue(self):
        return self.queueLine[-1]

    # Return queue length
    def get_queue_length(self):
        return len(self.queueLine)