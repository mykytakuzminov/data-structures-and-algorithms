import pytest
from data_structures.stacks.stack import Stack

# ====== Constants ======
NUM_ELEMENTS = 5
TEST_QUEUE = [n for n in range(NUM_ELEMENTS)]


# ====== Fixtures ======
@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def populated_stack():
    s = Stack()
    for n in range(NUM_ELEMENTS):
        s.push(n)
    return s


# ====== Tests: Emptiness ======
def test_is_empty(empty_stack, populated_stack):
    """Check is_empty() for empty and populated stacks."""
    assert empty_stack.is_empty()
    assert not populated_stack.is_empty()


# ====== Tests: Pushing Elements ======
def test_push(empty_stack):
    """Test push() adds elements to the end of the stack."""
    empty_stack.push(1)
    empty_stack.push(2)
    empty_stack.push(3)

    assert empty_stack.peek() == 3
    assert len(empty_stack) == 3


# ====== Tests: Popping Elements ======
def test_pop(populated_stack):
    """Test pop() removes and returns elements from the end."""
    assert populated_stack.pop() == TEST_QUEUE[-1]
    assert populated_stack.pop() == TEST_QUEUE[-2]
    assert populated_stack.pop() == TEST_QUEUE[-3]
    assert len(populated_stack) == NUM_ELEMENTS - 3


def test_pop_index_error(empty_stack):
    """Test pop() raises IndexError when the stack is empty."""
    with pytest.raises(IndexError):
        empty_stack.pop()


# ====== Tests: Accessing Elements ======
def test_peek(populated_stack):
    """Test peek() returns the last element without removing it."""
    assert populated_stack.peek() == TEST_QUEUE[-1]
    assert populated_stack.peek() == TEST_QUEUE[-1]
    assert len(populated_stack) == NUM_ELEMENTS


def test_peek_index_error(empty_stack):
    """Test peek() raises IndexError when the stack is empty."""
    with pytest.raises(IndexError):
        empty_stack.peek()


# ====== Tests: Clearing the List ======
def test_clear(empty_stack, populated_stack):
    """Check clear() empties the stack and resets length."""
    empty_stack.clear()
    assert empty_stack.traverse() == []
    assert len(empty_stack) == 0

    populated_stack.clear()
    assert populated_stack.traverse() == []
    assert len(populated_stack) == 0


# ====== Tests: Length & String Representation ======
def test_len(empty_stack, populated_stack):
    """Verify __len__() returns correct number of elements."""
    assert len(empty_stack) == 0
    assert len(populated_stack) == NUM_ELEMENTS


def test_str(empty_stack, populated_stack):
    """Check __str__ returns correct string representation of the stack."""
    assert str(empty_stack) == "Stack([])"
    assert str(populated_stack) == f"Stack({TEST_QUEUE})"
