class User:
    """User class for test execution"""

    def __init__(self, username, email, password, role="USER"):
        self.username = username
        self.email = email
        self.__password = password
        self.role = role  # USER, ADMIN, TESTER
        self.is_active = True
        self.test_cases_executed = 0

    def verify_password(self, password):
        return password == self.__password

    def increment_tests(self):
        self.test_cases_executed += 1

    def get_info(self):
        return (
            f"{self.username} ({self.role}) - {self.test_cases_executed} tests executed"
        )


class TestCase:
    """Enhanced TestCase class"""

    def __init__(self, id, title, expected, executed_by=None):
        self.id = id
        self.title = title
        self.expected = expected
        self.actual = None
        self.status = "PENDING"
        self.executed_by = executed_by

    def execute(self, actual_result):
        self.actual = actual_result
        self.status = "PASS" if self.actual == self.expected else "FAIL"
        if self.executed_by:
            self.executed_by.increment_tests()


class TestPlan:
    """Collection of test cases & execution tracking"""

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.test_cases = []
        self.created_date = "2026-05-22"

    def add_test_case(self, test_case):
        self.test_cases.append(test_case)

    def get_report(self):
        total = len(self.test_cases)
        passed = sum(1 for tc in self.test_cases if tc.status == "PASS")

        report = f"""
╔═════════════════════════════════════════════╗
║          TEST PLAN EXECUTION REPORT          ║
╠═════════════════════════════════════════════╣
║ Plan Name: {self.name}
║ Owner: {self.owner.username}
║ Total Tests: {total}
║ Passed: {passed}
║ Failed: {total - passed}
║ Pass Rate: {(passed/total)*100:.1f}% if total > 0 else 0
╠═════════════════════════════════════════════╣
"""
        for tc in self.test_cases:
            symbol = "✅" if tc.status == "PASS" else "❌"
            report += f"║ {symbol} {tc.id}: {tc.status}\n"

        report += "╚═════════════════════════════════════════════╝"
        return report


# Create users
qa_john = User("john_qa", "john@test.com", "password123", "TESTER")
qa_alice = User("alice_qa", "alice@test.com", "password456", "TESTER")

# Create test cases
tc1 = TestCase("TC001", "Valid login", "Success", qa_john)
tc2 = TestCase("TC002", "Invalid password", "Error", qa_alice)
tc3 = TestCase("TC003", "Locked account", "Locked message", qa_john)

# Execute tests
tc1.execute("Success")  # PASS
tc2.execute("Error")  # PASS
tc3.execute("Locked message")  # PASS

# Create test plan
plan = TestPlan("Login Feature Tests", qa_john)
plan.add_test_case(tc1)
plan.add_test_case(tc2)
plan.add_test_case(tc3)

# Print reports
print(plan.get_report())
print(f"\nQA Summary:")
print(f"  {qa_john.get_info()}")
print(f"  {qa_alice.get_info()}")

# Output should show:
# - Test plan with all 3 tests PASS
# - John executed 2 tests
# - Alice executed 1 test
