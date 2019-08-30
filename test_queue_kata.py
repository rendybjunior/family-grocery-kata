from queue_kata import Customer, Queue

def test_firstlast_happypath():
    customer_queue = Queue()

    customer_queue.add_queue(Customer(1, 6, ["biscuit", "chips"]))
    customer_queue.add_queue(Customer(2, 23, ["milk"]))
    customer_queue.add_queue(Customer(3, 55, ["soap"]))

    assert customer_queue.first().id == 1
    assert customer_queue.last().id == 3

def test_len():
    customer_queue = Queue()

    assert customer_queue.length() == 0

    customer_queue.add_queue(Customer(1, 6, ["biscuit", "chips"]))

    assert customer_queue.length() == 1

    for i in range(10):
        customer_queue.add_queue(Customer(1, 6, ["biscuit", "chips"]))

    assert customer_queue.length() == 11

def test_senior_citizens():
    customer_queue = Queue()

    customer_queue.add_queue(Customer(1, 6, ["biscuit", "chips"]))
    customer_queue.add_queue(Customer(2, 43, ["milk"]))
    customer_queue.add_queue(Customer(3, 55, ["soap"]))
    customer_queue.add_queue(Customer(4, 70, ["bread"]))
    customer_queue.add_queue(Customer(5, 34, ["milk"]))
    customer_queue.add_queue(Customer(6, 62, ["soap"]))

    assert [cust.id for cust in customer_queue.queue] == [4, 6, 1, 2, 3, 5]

def test_all_seniors():
    customer_queue = Queue()

    customer_queue.add_queue(Customer(1, 62, ["biscuit", "chips"]))
    customer_queue.add_queue(Customer(2, 63, ["milk"]))
    customer_queue.add_queue(Customer(3, 77, ["soap"]))
    customer_queue.add_queue(Customer(4, 70, ["bread"]))
    customer_queue.add_queue(Customer(5, 78, ["milk"]))
    customer_queue.add_queue(Customer(6, 63, ["soap"]))

    assert [cust.id for cust in customer_queue.queue] == [1,2,3,4,5,6]

def test_prohibited_items():
    customer_queue = Queue()

    customer_queue.add_queue(Customer(1, 16, ["biscuit", "chips", "alcohol"]))
    customer_queue.add_queue(Customer(2, 43, ["milk"]))
    customer_queue.add_queue(Customer(3, 76, ["alcohol"]))
    customer_queue.add_queue(Customer(4, 12, ["pencil"]))
    customer_queue.add_queue(Customer(5, 34, ["milk"]))
    customer_queue.add_queue(Customer(6, 88, ["soap"]))

    assert [cust.id for cust in customer_queue.queue] == [6, 2, 4, 5]

def test_all_prohibited():
    customer_queue = Queue()

    customer_queue.add_queue(Customer(1, 16, ["biscuit", "chips", "alcohol"]))
    customer_queue.add_queue(Customer(3, 76, ["alcohol"]))

    assert [cust.id for cust in customer_queue.queue] == []

def test_priority_of_age():
    customer_queue = Queue()

    customer_queue.add_queue(Customer(1, 16, ["biscuit", "chips", "alcohol"]))
    customer_queue.add_queue(Customer(2, 20, ["alcohol"]))
    customer_queue.add_queue(Customer(3, 63, ["alcohol 70%", "soap"]))
    customer_queue.add_queue(Customer(4, 76, ["hand sanitizer", "vitamin"]))
    customer_queue.add_queue(Customer(5, 30, ["battery", "sparkling water", "bread"]))

    assert [cust.id for cust in customer_queue.queue] == [3, 4, 2, 5]