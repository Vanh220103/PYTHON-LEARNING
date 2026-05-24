class TestCase:
    """Class để represent một test case"""

    # Class variable (shared across all instances)
    total_test_cases = 0

    def __init__(self, id, title, priority="MEDIUM"):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = "PENDING"
        self.steps = []
        self.expected_result = ""
        self.actual_result = ""
        TestCase.total_test_cases += 1

    def add_step(self, step_number, description):
        """Thêm step vào test case"""
        step = f"Step {step_number}: {description}"
        self.steps.append(step)

    def set_expected_result(self, result):
        """Set expected result"""
        self.expected_result = result

    def set_actual_result(self, result):
        """Set actual result"""
        self.actual_result = result

    def execute(self):
        """Mark test case as executed"""
        self.status = "EXECUTED"

    def mark_pass(self):
        """Mark test case as PASS"""
        if self.actual_result == self.expected_result:
            self.status = "PASS"
            return True
        else:
            self.status = "FAIL"
            return False

    def get_summary(self):
        """Lấy tóm tắt test case"""
        summary = f"""
═══════════════════════════════════════════════════════════
Test Case: {self.id} - {self.title}
Priority: {self.priority}
Status: {self.status}
───────────────────────────────────────────────────────────
Steps:
"""
        for step in self.steps:
            summary += f"  {step}\n"

        summary += f"""
Expected Result: {self.expected_result}
Actual Result: {self.actual_result}
═══════════════════════════════════════════════════════════
"""
        return summary


# Test
tc1 = TestCase("TC001", "Login with valid credentials", "CRITICAL")
tc1.add_step(1, "Enter username 'testuser'")
tc1.add_step(2, "Enter password 'pass123'")
tc1.add_step(3, "Click Login button")
tc1.set_expected_result("Redirect to dashboard")
tc1.set_actual_result("Redirect to dashboard")
tc1.execute()
tc1.mark_pass()

print(tc1.get_summary())

# Create more test cases
tc2 = TestCase("TC002", "Login with invalid password", "HIGH")
tc2.add_step(1, "Enter username 'testuser'")
tc2.add_step(2, "Enter password 'wrongpass'")
tc2.add_step(3, "Click Login button")
tc2.set_expected_result("Error message displayed")
tc2.set_actual_result("Error message displayed")
tc2.mark_pass()

print(tc2.get_summary())

# Check class variable
print(f"Total test cases created: {TestCase.total_test_cases}")
