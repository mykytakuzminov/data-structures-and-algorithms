import pytest
from data_structures.linked_lists.singly_linked_list import SinglyLinkedList

# ====== Constans ======
NUM_ELEMENTS = 5
TEST_LIST = [i for i in range(5)]

# ====== Fixtures ======
@pytest.fixture
def empty_list():
    """Return an empty singly linked list"""
    return SinglyLinkedList()

@pytest.fixture
def populated_list():
    """Return a singly linked list pre-populated with values"""
    sll = SinglyLinkedList()
    for value in TEST_LIST:
        sll.append(value)
    return sll

# ======= Tests ========
def test_is_empty(empty_list):
    """Test that is_empty() returns True for an empty list"""
    assert empty_list.is_empty()

def test_append(empty_list):
    """Test that append() adds element to the end of the list"""
    empty_list.append(NUM_ELEMENTS)
    assert empty_list.traverse() == [NUM_ELEMENTS]
    assert len(empty_list) == 1

def test_prepend(populated_list):
    """Test that prepend() adds element to the beginning of the list"""
    populated_list.prepend(NUM_ELEMENTS)
    assert populated_list.traverse() == [NUM_ELEMENTS] + TEST_LIST
    assert len(populated_list) == NUM_ELEMENTS + 1

def test_insert(populated_list):
    """Test that insert() adds an element at a specific index"""
    populated_list.insert(2, NUM_ELEMENTS)
    expected = TEST_LIST[:2] + [NUM_ELEMENTS] + TEST_LIST[2:]
    assert populated_list.traverse() == expected
    assert len(populated_list) == NUM_ELEMENTS + 1

def test_insert_index_error(populated_list):
    """Test that insert() raises IndexError for invalid indices"""
    with pytest.raises(IndexError):
        populated_list.insert(-1, NUM_ELEMENTS)
    with pytest.raises(IndexError):
        populated_list.insert(NUM_ELEMENTS + 1, NUM_ELEMENTS)

def test_delete(populated_list):
    """Test that delete() correctly removes existing and non-existing elements"""
    assert populated_list.delete(TEST_LIST[-1])
    assert not populated_list.delete(NUM_ELEMENTS)

def test_get(populated_list):
    """Test that get() returns correct element for valid indices"""
    assert populated_list.get(0) == TEST_LIST[0]
    assert populated_list.get(NUM_ELEMENTS - 1) == TEST_LIST[-1]

def test_get_index_error(populated_list):
    """Test that get() raises IndexError for invalid indices"""
    with pytest.raises(IndexError):
        populated_list.get(-1)
    with pytest.raises(IndexError):
        populated_list.get(NUM_ELEMENTS)

def test_search(populated_list):
    """Test that search() correctly identifies existing and non-existing elements"""
    assert populated_list.search(TEST_LIST[0])
    assert not populated_list.search(NUM_ELEMENTS)

def test_traverse_empty(empty_list):
    """Test that traverse() returns an empty list for an empty linked list"""
    assert empty_list.traverse() == []

def test_traverse_populated(populated_list):
    """Test that traverse() returns all elements in correct order for a populated list"""
    assert populated_list.traverse() == TEST_LIST

def test_clear(populated_list):
    """Test that clear() empties the list and resets its length to 0"""
    populated_list.clear()
    assert populated_list.traverse() == []
    assert len(populated_list) == 0

def test_len(populated_list):
    """Test that __len__() returns correct number of elements"""
    assert len(populated_list) == NUM_ELEMENTS

def test_str(populated_list):
    """Test that __str__() returns string representation of list"""
    assert str(populated_list) == str(TEST_LIST)
