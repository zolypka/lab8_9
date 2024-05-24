from three import roman_to_arabic

def test_roman_to_arabic():
    assert roman_to_arabic("III") == 3
    assert roman_to_arabic("IX") == 9
    assert roman_to_arabic("XLII") == 42
    assert roman_to_arabic("MCMXCIV") == 1994
