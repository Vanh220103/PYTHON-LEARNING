# Yêu cầu:
# 1. Tạo dictionary lưu test case
# 2. Thêm, modify, in kết quả

test_cases = {
    "id": 1,
    "title": "test case 1", 
    "status": "pass",
    "severity": "high"
}

print("Add into test cases: ")
test_cases["executed date"] = "22/05/2026"

print("Test cases after adding: ")
print(test_cases)

print("Modify test cases's status:")
test_cases["status"] = "fail"
print("Test cases after modifying: ")
print(test_cases)