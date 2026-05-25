import random

fullname = input("Nhập tên bệnh nhân: ")
sex = input("Nhập giới tính: ")
birthday = int(input("Nhập năm sinh: "))
phone = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symptom = input("Nhập triệu chứng ban đầu: ")
price = float(input("Nhập chi phí khám: "))

int1 = random.randint(0, 9)
int2= random.randint(0, 9)
int3 = random.randint(0, 9)
id = f"BN{birthday}{int1}{int2}{int3}"

print("--- THẺ BỆNH NHÂN ---")
print("Mã BN:", id, end="\n")

print("Tên:", fullname, "(" + type(fullname).__name__ + ")")
print("Giới tính:", sex, "(" + type(sex).__name__ + ")")
print("Năm sinh:", birthday, "(" + type(birthday).__name__ + ")")
print("Điện thoại:", phone, "(" + type(phone).__name__ + ")")
print("Email:", email, "(" + type(email).__name__ + ")")
print("Triệu chứng:", symptom, "(" + type(symptom).__name__ + ")")
print("Chi phí:", price, "(" + type(price).__name__ + ")")
