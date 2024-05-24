from one import longestCommonPrefix

def test_longestCommonPrefix_empty_list():
    assert longestCommonPrefix([]) == ""

def test_longestCommonPrefix_single_word():
    assert longestCommonPrefix(["apple"]) == "apple"

def test_longestCommonPrefix_same_words():
    assert longestCommonPrefix(["hello", "hello", "hello"]) == "hello"

def test_longestCommonPrefix_different_words():
    assert longestCommonPrefix(["flower", "flight", "floor"]) == "fl"

def test_longestCommonPrefix_empty_string():
    assert longestCommonPrefix(["", "abc", "def"]) == ""

def test_longestCommonPrefix_mixed_case():
    assert longestCommonPrefix(["python", "pyramid", "pythagoras"]) == "py"