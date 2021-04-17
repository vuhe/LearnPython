def check_for_repetition(a_list) -> bool:
    check = set(a_list)
    return len(check) != len(a_list)


test_list = [1, 2, 3, 4, 5, 5]
print(check_for_repetition(test_list))
