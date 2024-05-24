from two import find_missing_number

def test_find_missing_number():
    assert find_missing_number([1, 2, 4, 5], 5) == 3
    assert find_missing_number([3, 7, 1, 2, 8, 4, 5], 8) == 6