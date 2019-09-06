from queue_kata import Customer, Queue

def test_firstlast_happypath():
    q = Queue()

    q.addQueue(Customer(1, 6, ["biscuit", "chips"]))
    q.addQueue(Customer(2, 23, ["milk"]))
    q.addQueue(Customer(3, 55, ["soap"]))

    assert q.first().id == 1
    assert q.last().id == 3

def test_len():
    q = Queue()

    assert q.length() == 0

    q.addQueue(Customer(1, 6, ["biscuit", "chips"]))

    assert q.length() == 1

    for i in range(10):
        q.addQueue(Customer(1, 6, ["biscuit", "chips"]))

    assert q.length() == 11

def test_senior_citizens():
    q = Queue()

    q.addQueue(Customer(1, 6, ["biscuit", "chips"]))
    q.addQueue(Customer(2, 43, ["milk"]))
    q.addQueue(Customer(3, 55, ["soap"]))
    q.addQueue(Customer(4, 70, ["bread"]))
    q.addQueue(Customer(5, 34, ["milk"]))
    q.addQueue(Customer(6, 62, ["soap"]))

    assert [cust.id for cust in q.queue] == [4, 6, 1, 2, 3, 5]

def test_all_seniors():
    q = Queue()

    q.addQueue(Customer(1, 62, ["biscuit", "chips"]))
    q.addQueue(Customer(2, 63, ["milk"]))
    q.addQueue(Customer(3, 77, ["soap"]))
    q.addQueue(Customer(4, 70, ["bread"]))
    q.addQueue(Customer(5, 78, ["milk"]))
    q.addQueue(Customer(6, 63, ["soap"]))

    assert [cust.id for cust in q.queue] == [1,2,3,4,5,6]

def test_prohibited_items():
    q = Queue()

    q.addQueue(Customer(1, 16, ["biscuit", "chips", "alcohol"]))
    q.addQueue(Customer(2, 43, ["milk"]))
    q.addQueue(Customer(3, 76, ["alcohol"]))
    q.addQueue(Customer(4, 12, ["pencil"]))
    q.addQueue(Customer(5, 34, ["milk"]))
    q.addQueue(Customer(6, 88, ["soap"]))

    assert [cust.id for cust in q.queue] == [6, 2, 4, 5]


def test_all_prohibited():
    q = Queue()

    q.addQueue(Customer(1, 16, ["biscuit", "chips", "alcohol"]))
    q.addQueue(Customer(3, 76, ["alcohol"]))

    assert [cust.id for cust in q.queue] == []
