class Customer:
    def __init__(self, id, age, items):
        self.id = id
        self.age = age
        self.items = items # list of string

class CustomerAgeRange:
    def __init__(self, invalid_item):
        self.invalid_item = invalid_item
        self.age_ranges = self.init_age_ranges()
    
    def init_age_ranges(self):
        ageRanges = []
        age_0_to_18 = {
                "MinInclusiveAge":0, 
                "MaxExclusiveAge":18, 
                "InvalidItem":self.invalid_item,
                "IsPriority":False
                }

        age_18_to_62 = {
                "MinInclusiveAge":18, 
                "MaxExclusiveAge":62, 
                "InvalidItem":None,
                "IsPriority":False
                }

        age_62_to_max = {
                "MinInclusiveAge":62, 
                "MaxExclusiveAge":1000, 
                "InvalidItem":self.invalid_item,
                "IsPriority":True
                }

        ageRanges.append(age_0_to_18)
        ageRanges.append(age_18_to_62)
        ageRanges.append(age_62_to_max)
        return ageRanges 

    def get_age_range(self, age):
        for age_range in self.age_ranges:
            if (age >= age_range.get("MinInclusiveAge") 
                    and age < age_range.get("MaxExclusiveAge")):
                return age_range
                

class Queue:
    def __init__(self, invalid_items=["cigarette", "alcohol"]):
        self.items = []
        self.invalid_items = ["cigarette", "alcohol"]
        # self.under_age = 18
        self.senior_age = 62

    def is_valid_items(self, customer, invalid_items):
        if invalid_items is None:
            return True

        for item in customer.items:
            if item in self.invalid_items:
                return False
        return True

    # Add new item
    def add_item(self, customer):
        customerAgeRange = CustomerAgeRange(self.invalid_items) 
        ageRange = customerAgeRange.get_age_range(customer.age)

        if not self.is_valid_items(customer, ageRange.get("InvalidItem")):
            return

        if ageRange.get("IsPriority"):
            pos = 0
            i = 0
            while i < len(self.items) and self.items[i].age >= ageRange.get("MinInclusiveAge"):
                i += 1
            self.items.insert(i, customer)
        else:
            self.items.append(customer)

    # Return first item
    def first(self):
        return self.items[0]

    # Return last item
    def last(self):
        return self.items[-1]

    # Return queue length
    def length(self):
        return len(self.items)