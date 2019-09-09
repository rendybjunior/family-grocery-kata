class Customer:
    def __init__(self, id, age, groceries):
        self.id = id
        self.age = age
        self.groceries = groceries

class QueueSeniorPrioritization:
    
    PROHIBITED_GROCERIES = ["cigarette", "alcohol"]
    SENIOR_AGE_THRESHOLD = 62
    ADULT_AGE_THRESHOLD = 18
    LAST_SENIOR_QUEUE_INDEX = 0

    def __init__(self):
        self.queueLine = []

    def add_to_queue(self, customer):

        def _is_senior(age):
            return age >= QueueSeniorPrioritization.SENIOR_AGE_THRESHOLD
        
        def _is_adult(age):
            return age >= QueueSeniorPrioritization.ADULT_AGE_THRESHOLD

        def _remove_prohobited_grocery(groceries):
            for grocery in groceries:
                if grocery in QueueSeniorPrioritization.PROHIBITED_GROCERIES:
                    groceries.remove(grocery)

        if not _is_senior(customer.age):
            if not _is_adult(customer.age):
                _remove_prohobited_grocery(customer.groceries)
            if len(customer.groceries) is not 0:
                self.queueLine.append(customer)
        if _is_senior(customer.age):
            _remove_prohobited_grocery(customer.groceries)
            if len(customer.groceries) is not 0:
                while QueueSeniorPrioritization.LAST_SENIOR_QUEUE_INDEX < len(self.queueLine) and _is_senior(self.queueLine[QueueSeniorPrioritization.LAST_SENIOR_QUEUE_INDEX].age):
                    QueueSeniorPrioritization.LAST_SENIOR_QUEUE_INDEX += 1
                self.queueLine.insert(QueueSeniorPrioritization.LAST_SENIOR_QUEUE_INDEX, customer)

    def get_first_queue(self):
        return self.queueLine[0]

    def get_last_queue(self):
        return self.queueLine[-1]

    def get_queue_length(self):
        return len(self.queueLine)