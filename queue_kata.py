class Customer:
    def __init__(self, id, age, groceries):
        self.id = id
        self.age = age
        self.groceries = groceries

class QueueSeniorPrioritization:
    
    PROHIBITED_GROCERIES = ["cigarette", "alcohol"]
    SENIOR_AGE_THRESHOLD = 62
    UNDER_AGE_THRESHOLD = 18


    def __init__(self):
        self.queueLine = []
        self.last_senior_queue_index = 0

    def add_to_queue(self, customer):

        def _is_senior(age):
            return age >= QueueSeniorPrioritization.SENIOR_AGE_THRESHOLD
        
        def _is_under_age(age):
            return age <= QueueSeniorPrioritization.UNDER_AGE_THRESHOLD

        def _remove_prohobited_grocery(groceries):
            for grocery in groceries:
                if grocery in QueueSeniorPrioritization.PROHIBITED_GROCERIES:
                    groceries.remove(grocery)

        if not _is_senior(customer.age):
            if not _is_under_age(customer.age):
                _remove_prohobited_grocery(customer.groceries)
            if len(customer.groceries) is not 0:
                self.queueLine.append(customer)
        if _is_senior(customer.age):
            _remove_prohobited_grocery(customer.groceries)
            if len(customer.groceries) is not 0:
                while self.last_senior_queue_index < len(self.queueLine) and _is_senior(self.queueLine[self.last_senior_queue_index].age):
                    self.last_senior_queue_index += 1
                self.queueLine.insert(self.last_senior_queue_index, customer)

    def get_first_queue(self):
        return self.queueLine[0]

    def get_last_queue(self):
        return self.queueLine[-1]

    def get_queue_length(self):
        return len(self.queueLine)