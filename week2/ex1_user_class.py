class User:
    """Class để represent một user"""

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Private
        self.is_authenticated = False

    def authenticate(self, password):
        """Kiểm tra password đúng không"""
        if password == self.__password:
            self.is_authenticated = True
            return True
        return False

    def change_password(self, old_password, new_password):
        """Đổi password"""
        if self.authenticate(old_password):
            self.__password = new_password
            return "Password changed successfully"
        return "Authentication failed"

    def get_user_info(self):
        """Trả về thông tin user"""
        return f"Username: {self.username}, Email: {self.email}"


# Test
user1 = User("john123", "john@example.com", "SecurePass123")

# Test authentication
print(user1.authenticate("SecurePass123"))  # True
print(user1.is_authenticated)  # True

print(user1.authenticate("WrongPassword"))  # False

# Test password change
print(user1.change_password("SecurePass123", "NewPass456"))  # Success message
print(user1.authenticate("NewPass456"))  # True

# Test get info
print(user1.get_user_info())  # Username: john123, Email: john@example.com
