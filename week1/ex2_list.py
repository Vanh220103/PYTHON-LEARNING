# Yêu cầu:
# 1. Tạo list test cases
# 2. Thêm, xóa, in list
# 3. Tính tổng test cases pass

test_cases = [
    "test case 1",
    "test case 2",
    "test case 3",
    "test case 4",
    "test case 5",
    "test case 6",
    "test case 7",
    "test case 8",
    "test case 9",
    "test case 10",
]

print("Add more test cases: ")
new_test_case = input("Enter a new test case: ")
test_cases.append(new_test_case)

print("Delete test cases existed in the list: ")
chosen_test_case = input("Enter a test case to delete: ")
test_cases.remove(chosen_test_case)
print("Current test cases: ")
print(test_cases)

test_case_length = len(test_cases)
print(f"Total test cases: {test_case_length}")