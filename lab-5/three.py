def get_roman_input():
    user_input = input("Enter a roman number: ")
    return user_input

def roman_to_arabic(s=''):
    roman_dict = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    arabic = 0
    if s == '' or type(s) != str:
        return 'Invalid Entry'
    else:
        prev_value = 0
        for i in s[::-1]:
            if i in roman_dict:
                if roman_dict[i] < prev_value:
                    arabic -= roman_dict[i]
                else:
                    arabic += roman_dict[i]
                prev_value = roman_dict[i]
            else:
                return 'Invalid Entry'
        return arabic


if __name__ == "__main__":
    user_input = get_roman_input()
    print(roman_to_arabic(user_input))