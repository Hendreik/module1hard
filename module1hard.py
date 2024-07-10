# Дополнительное практическое задание по модулю: "Базовые структуры данных."
import main

main.print_hi('module1hard.py')  # .print_hi("PC")

# Задание "Средний балл":
# На вход даны следующие данные:
# Список:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество:
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
#
# dict1 = zip(students,grades)
dict1 = {}
for n in range(students.__len__()):
	grd = 0
	print(sum(grades[n]))
	dict1.update({students[n]: sum(grades[n]) / len(grades[n])})
# print(students)
# print(grades)

print(dict1)
