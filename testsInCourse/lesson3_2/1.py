import self

assert abs(-42) == 42, "Should be absolute value of a number"

print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")




"""def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        f"expected {expected_result}, got {actual_result}"
expected_result = 8
actual_result = 11

test_input_text(expected_result, actual_result)"""


s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')


def test_substring(full_string, substring):
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"


