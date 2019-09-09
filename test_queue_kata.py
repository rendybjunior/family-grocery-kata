from queue_kata import Customer, QueueSeniorPrioritization

def test_firstlast_happypath():
    q = QueueSeniorPrioritization()

    q.add_to_queue(Customer(1, 6, ["biscuit", "chips"]))
    q.add_to_queue(Customer(2, 23, ["milk"]))
    q.add_to_queue(Customer(3, 55, ["soap"]))

    assert q.get_first_queue().id == 1
    assert q.get_last_queue().id == 3

def test_len():
    q = QueueSeniorPrioritization()

    assert q.get_queue_length() == 0

    q.add_to_queue(Customer(1, 6, ["biscuit", "chips"]))

    assert q.get_queue_length() == 1

    for i in range(10):
        q.add_to_queue(Customer(1, 6, ["biscuit", "chips"]))

    assert q.get_queue_length() == 11

def test_senior_citizens():
    q = QueueSeniorPrioritization()

    q.add_to_queue(Customer(1, 6, ["biscuit", "chips"]))
    q.add_to_queue(Customer(2, 43, ["milk"]))
    q.add_to_queue(Customer(3, 55, ["soap"]))
    q.add_to_queue(Customer(4, 70, ["bread"]))
    q.add_to_queue(Customer(5, 34, ["milk"]))
    q.add_to_queue(Customer(6, 62, ["soap"]))

    assert [cust.id for cust in q.queue_line] == [4, 6, 1, 2, 3, 5]

def test_all_seniors():
    q = QueueSeniorPrioritization()

    q.add_to_queue(Customer(1, 62, ["biscuit", "chips"]))
    q.add_to_queue(Customer(2, 63, ["milk"]))
    q.add_to_queue(Customer(3, 77, ["soap"]))
    q.add_to_queue(Customer(4, 70, ["bread"]))
    q.add_to_queue(Customer(5, 78, ["milk"]))
    q.add_to_queue(Customer(6, 63, ["soap"]))

    assert [cust.id for cust in q.queue_line] == [1,2,3,4,5,6]

def test_prohibited_items():
    q = QueueSeniorPrioritization()

    q.add_to_queue(Customer(1, 16, ["biscuit", "chips", "alcohol"]))
    q.add_to_queue(Customer(2, 43, ["milk"]))
    q.add_to_queue(Customer(3, 76, ["alcohol"]))
    q.add_to_queue(Customer(4, 12, ["pencil"]))
    q.add_to_queue(Customer(5, 34, ["milk"]))
    q.add_to_queue(Customer(6, 88, ["soap"]))

    assert [cust.id for cust in q.queue_line] == [6, 1, 2, 4, 5]


def test_all_prohibited():
    q = QueueSeniorPrioritization()

    q.add_to_queue(Customer(1, 16, ["biscuit", "chips", "alcohol"]))
    q.add_to_queue(Customer(3, 76, ["alcohol"]))

    assert [cust.id for cust in q.queue_line] == [1]
