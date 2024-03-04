'''
Особенности данной программы:
- выдает случайный номер билета студента
- формирует список с номерами всех выданных билетов
- минимизирует повторения билетов (уникальные билеты на каждые 17 учеников)
'''
import random
def reset_biletsy():
    global biletsy
    biletsy = list(range(1, 18))
    random.shuffle(biletsy)

def give_bilet_number(name):
    if not biletsy: # если билеты кончились то запускает функц ресета
        reset_biletsy()

    bilet_number = random.choice(biletsy)
    biletsy.remove(bilet_number)

    return f"{name}, ваш номер билета {bilet_number}."

biletsy = list(range(1, 18))
all_results = []

num_students = int(input("Количество присутствующих студентов на экзамене: ")) # 1 вар. ограничитель
#num_students = 200 # 2 вар. сколько студентов будет вводить свое имя и получать билеты

for i in range(num_students):
    student_name = input("Введите свое имя и фамилию: ")
    result = give_bilet_number(student_name)
    if result is not None: # подстраховка чтоб пустые результаты не записывал
        all_results.append(result) # сохраняет все назначенные билеты в один список
        print(result)
    else: # подстраховка
        break

print("\n--- Все билеты ---")
for result in all_results:
    print(result)