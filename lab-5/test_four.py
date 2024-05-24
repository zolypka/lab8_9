from four import are_anagrams

def test_are_anagrams():
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("debit card", "bad credit") == True
