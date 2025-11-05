import pytest
from data_structures.linked_lists.doubly_linked_list import DoublyLinkedList

# ====== Constans ======
NUM_ELEMENTS = 5
TEST_LIST = [i for i in range(5)]
NEW_HEAD = 99
NEW_MIDDLE = 55
NEW_TAIL = 100
INVALID_LOW_INDEX = -1
INVALID_HIGH_INDEX = NUM_ELEMENTS + 1
NOT_EXISTING_VALUE = 999
NOT_EXISTING_VALUES = [NUM_ELEMENTS, NEW_HEAD, NEW_MIDDLE, NEW_TAIL, NOT_EXISTING_VALUE]

testdata = [(i, val) for i, val in enumerate(TEST_LIST)]

# ====== Fixtures ======
@pytest.fixture
def empty_list():
    """Return an empty doubly linked list"""
    return DoublyLinkedList()

@pytest.fixture
def populated_list():
    """Return a doubly linked list pre-populated with values"""
    dll = DoublyLinkedList()
    for value in TEST_LIST:
        dll.append(value)
    return dll

# ====== Tests ======
def test_is_empty(empty_list, populated_list):
    """Test that is_empty() returns True for an empty list"""
    assert empty_list.is_empty()
    assert not populated_list.is_empty()

def test_append(empty_list):
    """Test that append() adds element to the end of the list"""
    empty_list.append(1)
    empty_list.append(2)
    empty_list.append(3)
    assert empty_list.traverse() == [1, 2, 3]
    assert len(empty_list) == 3
    assert empty_list._get_head().data == 1
    assert empty_list._get_tail().data == 3

def test_prepend(empty_list, populated_list):
    """Test that prepend() adds element to the beginning of the list"""
    empty_list.prepend(NEW_HEAD)
    assert empty_list.traverse() == [NEW_HEAD]
    assert len(empty_list) == 1
    assert empty_list._get_head().data == NEW_HEAD
    assert empty_list._get_tail().data == NEW_HEAD

    populated_list.prepend(NEW_HEAD)
    assert populated_list.traverse() == [NEW_HEAD] + TEST_LIST
    assert len(populated_list) == NUM_ELEMENTS + 1
    assert populated_list._get_head().data == NEW_HEAD
    assert populated_list._get_tail().data == TEST_LIST[-1]

def test_insert(populated_list):
    """Test that insert() adds an element at a specific index"""
    populated_list.insert(0, NEW_HEAD)
    assert populated_list.traverse()[0] == NEW_HEAD

    middle_index = NUM_ELEMENTS // 2
    populated_list.insert(middle_index, NEW_MIDDLE)
    assert populated_list.traverse()[middle_index] == NEW_MIDDLE

    populated_list.insert(len(populated_list), NEW_TAIL)
    assert populated_list.traverse()[-1] == NEW_TAIL

    assert len(populated_list) == NUM_ELEMENTS + 3
    assert populated_list._get_head().data == NEW_HEAD
    assert populated_list._get_tail().data == NEW_TAIL

def test_insert_index_error(populated_list):
    """Test that insert() raises IndexError for invalid indices"""
    with pytest.raises(IndexError):
        populated_list.insert(INVALID_LOW_INDEX, NEW_MIDDLE)
    with pytest.raises(IndexError):
        populated_list.insert(INVALID_HIGH_INDEX, NEW_MIDDLE)

def test_delete(populated_list):
    """Test that delete() correctly removes existing and non-existing elements"""
    assert populated_list.delete(TEST_LIST[0])
    assert TEST_LIST[0] not in populated_list.traverse()

    assert populated_list.delete(TEST_LIST[2])
    assert TEST_LIST[2] not in populated_list.traverse()

    assert populated_list.delete(TEST_LIST[-1])
    assert TEST_LIST[-1] not in populated_list.traverse()

    assert not populated_list.delete(NOT_EXISTING_VALUE)
    assert populated_list._get_head().data == TEST_LIST[1]
    assert populated_list._get_tail().data == TEST_LIST[-2]

@pytest.mark.parametrize("index,expected", testdata)
def test_get(populated_list, index, expected):
    """Test that get() returns correct element for valid indices"""
    assert populated_list.get(index) == expected

def test_get_index_error(populated_list):
    """Test that get() raises IndexError for invalid indices"""
    with pytest.raises(IndexError):
        populated_list.get(INVALID_LOW_INDEX)
    with pytest.raises(IndexError):
        populated_list.get(INVALID_HIGH_INDEX)

@pytest.mark.parametrize("value", TEST_LIST)
def test_search_existing(populated_list, value):
    """Test that search() correctly identifies existing and non-existing elements"""
    assert populated_list.search(value)

@pytest.mark.parametrize("value", NOT_EXISTING_VALUES)
def test_search_not_existing(populated_list, value):
    """Test that search() correctly identifies existing and non-existing elements"""
    assert not populated_list.search(value)

def test_traverse_empty(empty_list):
    """Test that traverse() returns an empty list for an empty linked list"""
    assert empty_list.traverse() == []

def test_traverse_populated(populated_list):
    """Test that traverse() returns all elements in correct order for a populated list"""
    assert populated_list.traverse() == TEST_LIST

def test_links_integrity(populated_list):
    """Test that all 'next' and 'prev' pointers in the doubly linked list are consistent"""
    current = populated_list._get_head()
    while current.next:
        assert current.next.prev == current
        current = current.next

def test_clear(empty_list, populated_list):
    """Test that clear() empties the list and resets its length to 0"""
    empty_list.clear()
    assert empty_list.traverse() == []
    assert len(empty_list) == 0
    assert empty_list._get_head() is None
    assert empty_list._get_tail() is None

    populated_list.clear()
    assert populated_list.traverse() == []
    assert len(populated_list) == 0
    assert populated_list._get_head() is None
    assert populated_list._get_tail() is None

def test_len(empty_list, populated_list):
    """Test that __len__() returns correct number of elements"""
    assert len(empty_list) == 0
    assert len(populated_list) == NUM_ELEMENTS

def test_str(empty_list, populated_list):
    """Test that __str__() returns string representation of list"""
    assert str(empty_list) == str([])
    assert str(populated_list) == str(TEST_LIST)
