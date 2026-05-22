# Yêu cầu:
# 1. Lấy điểm số
# 2. Xác định grade (A/B/C/D/F)
# 3. In kết quả

score = float(input("Enter the score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The grade for the score {score} is {grade}.")