def get_input_array():
    arr_input = input("Enter the array: ")
    return [int(x) for x in arr_input.split()]

def find_missing_number(nums, n):
    total_sum = (n * (n + 1)) // 2
    remaining_sum = sum(nums)
    missing_number = total_sum - remaining_sum
    return missing_number


if __name__ == "__main__":
    arr = get_input_array()
    m = len(arr)
    n = m + 1
    print(find_missing_number(arr, n))