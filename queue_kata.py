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
        if x.age < 62:
            if x.age < 18:
                for item in x.items:
                    if item in ["cigarette", "alcohol"]:
                        return
            self.items.append(x)
        if x.age >=62:
            for item in x.items:
                if item in ["cigarette", "alcohol"]: # prohibited items
                    return
            pos = 0
            i = 0
            while i < len(self.items) and self.items[i].age >= 62:
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