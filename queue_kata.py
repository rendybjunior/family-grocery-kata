class Customer:
    def __init__(self, id, age, items):
        self.id = id
        self.age = age
        self.items = items # list of string

class Queue:
    def __init__(self):
        self.items = []

    # Add new item

    def add_item(self, x):

        special_items =[]
        special_items =["cigarette", "alcohol"]
        upper_treshold_age =62
        lower_treshold_age =18

        if x.age < upper_treshold_age:
            if x.age < lower_treshold_age:
                for item in x.items:
                    if item in special_items:
                        return
            self.items.append(x)
        if x.age >=upper_treshold_age:
            for item in x.items:
                if item in special_items: # prohibited items
                    return
            i = 0
            while i < len(self.items) and self.items[i].age >= upper_treshold_age:
                i += 1
            # print(i)
            self.items.insert(i, x)

    # Return first item
    def first(self):
        return self.items[0]

    # Return last item
    def last(self):
        return self.items[-1]

    # Return queue length
    def length(self):
        return len(self.items)
