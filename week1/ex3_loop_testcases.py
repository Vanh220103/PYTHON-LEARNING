# Yêu cầu:
# 1. Tạo list test cases với status
# 2. Lặp qua và in từng cái
# 3. Count pass/fail

test_cases = [
    {"id": "TC001", "title": "Login", "status": "PASS"},
    {"id": "TC002", "title": "Logout", "status": "PASS"},
    {"id": "TC003", "title": "Register", "status": "FAIL"},
    {"id": "TC004", "title": "Password reset", "status": "PASS"},
]

pass_count = 0
fail_count = 0

for test_case in test_cases:
    print(f"Test Case ID: {test_case['id']}, Title: {test_case['title']}, Status: {test_case['status']}")
    
    if test_case["status"] == "PASS":
        pass_count += 1
    else:
        fail_count += 1

print(f"Pass: {pass_count}, Fail: {fail_count}")
