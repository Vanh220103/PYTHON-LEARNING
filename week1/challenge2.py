# 1. Tạo dictionary chứa thông tin học sinh
# 2. Có tối thiểu 3 môn học với điểm
# 3. Tính điểm trung bình
# 4. Xác định vượt hay không vượt (>= 5.0 là pass)

student_info = {
    "name": "John Doe",
    "age": 20,
    "subjects": {"Math": 7.5, "English": 6.0, "Science": 8.0},
}

# Tính điểm trung bình
avg_score = sum(student_info["subjects"].values()) / len(student_info["subjects"])

if avg_score >= 5.0:
    print(f"{student_info['name']} passed with an average score of {avg_score:.2f}.")
else:
    print(f"{student_info['name']} failed with an average score of {avg_score:.2f}.")