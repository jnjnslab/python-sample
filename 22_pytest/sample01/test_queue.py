from strclass import Queue

def test_enqueue_01():
    a_queue = Queue()
    for i in range(5):
        a_queue.enqueue(i)
    assert a_queue.size() == 5

def test_dequeue_01():
    a_queue = Queue()
    for i in range(5):
        a_queue.enqueue(i)
    assert a_queue.dequeue() == 0