# Дополнительное практическое задание по модулю: "Базовые структуры данных."
import main

main.print_hi('module1hard.py')

# Задание "Средний балл":
# На вход даны следующие данные:
# Список:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество:
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
#
dict1 = dict({})
for n in range(students.__len__()):
	dict1.update({students[n]: sum(grades[n]) / len(grades[n])})

### out:
print('results ', dict1)
