import pytest
from data_structures.hash_tables.hash_map import HashMap

# ====== Constants ======
NUM_ELEMENTS = 10
KEY_5 = 5
KEY_10 = 10
NEW_VALUE = 100

TEST_PAIRS = [
    (0, 0), (8, 8), (1, 1), (9, 9), (2, 2),
    (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)
]

SET_OF_TEST_PAIRS = set([f"{k}: {v}" for k, v in TEST_PAIRS])

# ====== Fixtures ======
@pytest.fixture
def empty_hash_map():
    """Return an empty HashMap."""
    return HashMap()

@pytest.fixture
def populated_hash_map():
    """Return a HashMap filled with TEST_PAIRS."""
    hm = HashMap()
    for k, v in TEST_PAIRS:
        hm.put(k, v)
    return hm

# ====== Tests: Emptiness ======
def test_is_empty(empty_hash_map, populated_hash_map):
    """Check is_empty() for empty and populated HashMap."""
    assert empty_hash_map.is_empty()
    assert not populated_hash_map.is_empty()

# ====== Tests: Adding & Updating Keys ======
def test_put_not_existing_key(populated_hash_map):
    """Check inserting a new key increases length and stores value correctly."""
    populated_hash_map.put(KEY_10, NEW_VALUE)
    assert populated_hash_map.get(KEY_10) == NEW_VALUE
    assert len(populated_hash_map) == NUM_ELEMENTS + 1

def test_put_existing_key(populated_hash_map):
    """Check updating an existing key keeps length the same and updates value."""
    populated_hash_map.put(KEY_5, NEW_VALUE)
    assert populated_hash_map.get(KEY_5) == NEW_VALUE
    assert len(populated_hash_map) == NUM_ELEMENTS

def test_put_collision(empty_hash_map):
    """
    Test collisions: multiple keys hashing to the same bucket.
    For capacity=8, keys 0, 8, 16 hash to the same index.
    """
    empty_hash_map.put(0, 0)
    empty_hash_map.put(8, 8)
    empty_hash_map.put(16, 16)

    assert empty_hash_map.get(0) == 0
    assert empty_hash_map.get(8) == 8
    assert empty_hash_map.get(16) == 16

    assert len(empty_hash_map) == 3

# ====== Tests: Retrieving Values ======
@pytest.mark.parametrize("key,value", TEST_PAIRS)
def test_get_existing(populated_hash_map, empty_hash_map, key, value):
    """Check get() returns correct value for existing keys, None for missing keys."""
    assert populated_hash_map.get(key) == value
    assert empty_hash_map.get(key) == None

# ====== Tests: Removing Keys ======
def test_remove_existing_key(populated_hash_map):
    """Check removing an existing key decreases length and removes value."""
    assert populated_hash_map.remove(KEY_5)
    assert len(populated_hash_map) == NUM_ELEMENTS - 1
    assert populated_hash_map.get(KEY_5) is None

def test_remove_not_existing_key(populated_hash_map):
    """Check removing a non-existing key returns False and length stays same."""
    assert not populated_hash_map.remove(KEY_10)
    assert len(populated_hash_map) == NUM_ELEMENTS
    assert populated_hash_map.get(KEY_10) is None

# ====== Tests: Length & String Representation ======
def test_len(empty_hash_map, populated_hash_map):
    """Check __len__ returns correct number of elements."""
    assert len(empty_hash_map) == 0
    assert len(populated_hash_map) == NUM_ELEMENTS

def test_str(empty_hash_map, populated_hash_map):
    """Check __str__ returns correct string representation of the HashMap."""
    assert str(empty_hash_map) == "{}"

    actual_pairs = set(str(populated_hash_map).strip("{}").split(", "))
    assert actual_pairs == SET_OF_TEST_PAIRS
