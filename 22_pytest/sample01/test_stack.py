from strclass import Stack

def test_push_01():
    stack = Stack()
    for c in "Hello":
        stack.push(c)
    assert stack.size() == 5

def test_pop_01():
    stack = Stack()
    for c in "Hello":
        stack.push(c)
    assert stack.pop() == 'o'