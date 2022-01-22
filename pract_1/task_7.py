# 1. Змінній var_int надайте значення 10, var_float - значення 8.4, var_str - "No".
# 1. Змінній var_int надайте значення 10, var_float - значення 8.4, var_str - "No".
var_int = 10
var_float = 8.4
var_str = "No"

# 2. Змініть значення, збережене в змінної var_int, збільшивши його в 3.5 рази, результат зв'яжіть зі змінною var_big.
var_big = var_int * 3.5

# 3. Змініть значення, збережене в змінної var_float, зменшивши його на одиницю, результат зв'яжіть з тієї ж змінної.
var_float = var_float - 1

# 4. Розділіть var_int на var_float, а потім var_big на var_float. 5.Результат даних виразів не прив'язуйте до жодних змінних.
var_int / var_float
var_big / var_float

# 6. Виведіть значення всіх змінних.
print("var_int: ", var_int)
print("var_float: ", var_float)
print("var_str: ", var_str)
print("var_big: ", var_big)

# 7. Напишіть програму, яка запитувала б у користувача: 
    # - ПІБ ("Ваші прізвище, ім'я, по батькові?")
    # - вік ("Скільки Вам років?")
    # - місце проживання ("Де Ви живете?")
    # - де Ви навчаєтесь ("Де Ви навчаєтесь?”)
    # - номер Вашої групи( "Номер Вашої групи?”)
    # - порядковий номер по списку у группі("Який Ваш порядковий номер у списку групи?”)
    # - питання відповідно до варіанту: Як Ви себе почуваєте?
    # Після цього виводила б рядки:
    # "Ваше ім'я"
    # "Ваш вік"
    # "Ви живете в"
    # "Ви навчаєтесь в”.
    # "Номер моєї групи -”
    # "Мій порядковий номер у списку групи-" «Ваш варіант відповіді»

class Person:
    fullname = ""
    age = ""
    location = ""
    school = ""
    group_no = ""
    id = ""
    mood = ""

student = Person()

print("Ваші прізвище, ім'я, по батькові?")
student.fullname = input()
print("Скільки Вам років?")
student.age = input()
print("Де Ви живете?")
student.location = input()
print("Де Ви навчаєтесь?")
student.school = input()
print("Номер Вашої групи?")
student.group_no = input()
print("Який Ваш порядковий номер у списку групи?")
student.id = input()
print("питання відповідно до варіанту: Як Ви себе почуваєте?")
student.mood = input()

# output = """
# Ваше ім'я: %s
# Ваш вік: %s
# Ви живете в %s 
# Ви навчаєтесь в %s
# Номер моєї групи: %s
# Мій порядковий номер у списку групи: %s
# """%(student.fullname, student.age,student.location,student.school,student.group_no,student.id)

output = f"""
Ваше ім'я: {student.fullname}
Ваш вік: {student.age}
Ви живете в {student.location}
Ви навчаєтесь в {student.school}
Номер моєї групи: {student.group_no}
Мій порядковий номер у списку групи: {student.id}
"""


print(output)
