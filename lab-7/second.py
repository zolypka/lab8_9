def find_max_substring(search_query):
    search_query = search_query.lower()
    max_substring = ""
    max_count = 0

    for i in range(len(search_query)):
        for j in range(i + 1, len(search_query) + 1):
            substring = search_query[i:j]
            count = search_query.count(substring)

            if count > max_count or (count == max_count and len(substring) > len(max_substring)):
                max_substring = substring
                max_count = count

    return max_substring, max_count

def get_user_input():
    user_input = input("write a word: ")
    return user_input

if __name__ == "__main__":
    search_query = get_user_input()
    print("max subsring and its count: ",find_max_substring(search_query))