def get_input_words():
    input_words = input("Enter words separated by spaces: ").split()
    return input_words

def are_anagrams(*words):
    def normalize(word):
        return ''.join(sorted(word.lower()))

    normalized_words = [normalize(word) for word in words]
    return len(set(normalized_words)) == 1


if __name__ == "__main__":
    input_words = get_input_words()
    print(are_anagrams(*input_words))