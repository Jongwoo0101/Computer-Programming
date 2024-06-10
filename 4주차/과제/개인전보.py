s = input("학번과 이름, 학과번호를 순서대로 입력하세요: ")
student_id = s[:6]
department_id = s[-2:]
name = s[6:-2]
print(f"학과번호: {department_id}, 학번: {student_id}, 이름: {name}")