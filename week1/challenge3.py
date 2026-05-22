# Yêu cầu:

# Lấy input: cân nặng (kg) & chiều cao (cm)
# Tính BMI: BMI = weight (kg) / (height (m))^2
# Xác định status:

# BMI < 18.5: Underweight
# 18.5 - 24.9: Normal
# 25 - 29.9: Overweight


# = 30: Obese
weight = float(input("Enter weight (kg): "))
height_cm = float(input("Enter height (cm): "))

height_m = height_cm / 100
bmi = weight / (height_m**2)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print(f"Weight: {weight} kg")
print(f"Height: {height_cm} cm")
print(f"BMI: {bmi:.1f}")
print(f"Status: {status}")
