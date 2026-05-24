class TestCase:
    """Simplified TestCase class"""

    def __init__(self, id, title, expected):
        self.id = id
        self.title = title
        self.expected = expected
        self.actual = None
        self.status = "NOT_RUN"

    def run(self, actual_result):
        """Run test and compare"""
        self.actual = actual_result
        if self.actual == self.expected:
            self.status = "PASS"
        else:
            self.status = "FAIL"

    def __str__(self):
        return f"{self.id} - {self.title}: {self.status}"


class TestSuite:
    """Collection of test cases"""

    def __init__(self, name):
        self.name = name
        self.test_cases = []

    def add_test_case(self, test_case):
        """Add test case to suite"""
        self.test_cases.append(test_case)

    def run_all(self):
        """Run all test cases (simulate)"""
        for tc in self.test_cases:
            # Simulate execution
            # (In real automation, would run actual script)
            pass

    def get_summary(self):
        """Generate summary report"""
        total = len(self.test_cases)
        passed = sum(1 for tc in self.test_cases if tc.status == "PASS")
        failed = sum(1 for tc in self.test_cases if tc.status == "FAIL")

        summary = f"""
╔════════════════════════════════════════════════════════════╗
║                    TEST EXECUTION REPORT                   ║
╠════════════════════════════════════════════════════════════╣
║ Test Suite: {self.name}
║ Total Test Cases: {total}
║ Passed: {passed}
║ Failed: {failed}
║ Pass Rate: {(passed/total)*100:.1f}%
╠════════════════════════════════════════════════════════════╣
║ RESULTS:
"""
        for tc in self.test_cases:
            symbol = "✅" if tc.status == "PASS" else "❌"
            summary += f"║ {symbol} {tc}\n"

        summary += "╚════════════════════════════════════════════════════════════╝"
        return summary


# Create test suite
suite = TestSuite("Login Feature Tests")

# Create test cases
tc1 = TestCase("TC001", "Valid login", "Redirect to dashboard")
tc1.run("Redirect to dashboard")
suite.add_test_case(tc1)

tc2 = TestCase("TC002", "Invalid password", "Error message")
tc2.run("Error message")
suite.add_test_case(tc2)

tc3 = TestCase("TC003", "Empty username", "Validation error")
tc3.run("Login successful")  # Wrong result = FAIL
suite.add_test_case(tc3)

tc4 = TestCase("TC004", "Locked account", "Account locked message")
tc4.run("Account locked message")
suite.add_test_case(tc4)

# Print report
print(suite.get_summary())
