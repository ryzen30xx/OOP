import random

Student_names = []
IDs = []
grades = []

status = ""

def add_stu(name, grade):
	if name in Student_names:
		status = (f"{name} has been exist !")
	elif not name:
		status = ("Student input is blank !")
	else:
		Student_names.append(str(name))
		IDs.append(random.sample("123456789", 6))
		grades.append(grade)
		status = "Added Cuccessfully"

def edit_stu(name, id, grade):

	for i in range(len(IDs)):
		if id == IDs[i]:
			Student_names[i] += name # Student_names[i] = Student_names[i] + name
			grades[i] += grade
			status = (f"{id} has been updated name and grade to {name}, {grade}")

def del_stu(id):
	for i in range(len(IDs)):
		if id == IDs[i]:
			Student_names.pop(i)
			grades.pop(i)
			IDs.pop(i)

def search(part_name):
	for i in range(len(Student_names)):
		if part_name in Student_names[i]:
			print()

def show_all():
	count = 1
	for i in range(len(Student_names)):
		print(f"")
		count += 1

if __name__ == "__main__":
	running = True
	while running:
		print("Student manager tool\n\n")
		if error != "": print(f"Status: {status}"), status = ""
		print("1. Add Student\n2. Edit Student\n3. Delete Student\n4. Search by name\n5. Show all")
		choose = input("Please choose the function: ")
		if choose 0>= choose >=5:
			print("Wrong choose !")
		elif choose == 1:
			add_stu()
		elif choose == 2:
			edit_stu()
		elif choose == 3:
			del_stu()
		elif choose == 4:
			search()
		else choose == 5:
			show_all()
