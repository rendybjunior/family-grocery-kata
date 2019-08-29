from queue_kata import Customer, FamilyGroceryQueue

def test_firstlast_happypath():
    q = FamilyGroceryQueue()

    q.add_customer(Customer(1, 6, ["biscuit", "chips"]))
    q.add_customer(Customer(2, 23, ["milk"]))
    q.add_customer(Customer(3, 55, ["soap"]))

    assert q.first().id == 1
    assert q.last().id == 3

def test_len():
    q = FamilyGroceryQueue()

    assert q.length() == 0

    q.add_customer(Customer(1, 6, ["biscuit", "chips"]))

    assert q.length() == 1

    for i in range(10):
        q.add_customer(Customer(1, 6, ["biscuit", "chips"]))

    assert q.length() == 11

def test_senior_citizens():
    q = FamilyGroceryQueue()

    q.add_customer(Customer(1, 6, ["biscuit", "chips"]))
    q.add_customer(Customer(2, 43, ["milk"]))
    q.add_customer(Customer(3, 55, ["soap"]))
    q.add_customer(Customer(4, 70, ["bread"]))
    q.add_customer(Customer(5, 34, ["milk"]))
    q.add_customer(Customer(6, 62, ["soap"]))

    assert [cust.id for cust in q.customers] == [4, 6, 1, 2, 3, 5]

def test_all_seniors():
    q = FamilyGroceryQueue()

    q.add_customer(Customer(1, 62, ["biscuit", "chips"]))
    q.add_customer(Customer(2, 63, ["milk"]))
    q.add_customer(Customer(3, 77, ["soap"]))
    q.add_customer(Customer(4, 70, ["bread"]))
    q.add_customer(Customer(5, 78, ["milk"]))
    q.add_customer(Customer(6, 63, ["soap"]))

    assert [cust.id for cust in q.customers] == [1,2,3,4,5,6]

def test_prohibited_items():
    q = FamilyGroceryQueue()

    q.add_customer(Customer(1, 16, ["biscuit", "chips", "alcohol"]))
    q.add_customer(Customer(2, 43, ["milk"]))
    q.add_customer(Customer(3, 76, ["alcohol"]))
    q.add_customer(Customer(4, 12, ["pencil"]))
    q.add_customer(Customer(5, 34, ["milk"]))
    q.add_customer(Customer(6, 88, ["soap"]))

    assert [cust.id for cust in q.customers] == [6, 2, 4, 5]


def test_all_prohibited():
    q = FamilyGroceryQueue()

    q.add_customer(Customer(1, 16, ["biscuit", "chips", "alcohol"]))
    q.add_customer(Customer(3, 76, ["alcohol"]))

    assert [cust.id for cust in q.customers] == []
