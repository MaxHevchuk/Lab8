import enum


def averageAge(list_dict):  # Функ. для обчислення середнього віку
    sum_years = 0
    for diction in list_dict:
        sum_years += diction['years']
    return sum_years / len(list_dict)


def averageGender(list_dict):  # Функ. для обчислення середньостатистичні дані про стать
    sum_male, sum_female, sum_all = 0, 0, len(list_dict)
    for diction in list_dict:
        if diction['gender'] == 'Man':
            sum_male += 1
        elif diction['gender'] == 'Woman':
            sum_female += 1
    k_male = sum_male * 100 / sum_all
    k_female = sum_female * 100 / sum_all
    return k_male, k_female


class EyeColour(enum.Enum):  # Клас кольорів очей
    Blue = 1
    Brown = 2
    Green = 3


data_base = []
template = {'surname': '', 'years': 0, 'gender': '', 'eye': EyeColour(1)}  # Створюємо словник-зразок
print('1 - Блакитні очі\n2 - Карі\n3 - Зелені')
print('Приклад: Smith 34 Man 2')
print('Введіть дані про людей (Прізвище Вік Стать Колір очей) через пробіл, після нажміть Enter:')
while True:
    element = 0
    user_data = input('>>> ').split()  # Приймаємо дані від користувача
    if not user_data:  # Якщо користувач настиснув enter виходимо з циклу
        break
    try:
        if user_data[2] != ('Man' or 'Woman'):  # Якщо юзер не введе стать (або введе її не вірно) виведеться сповіщення
            print('Введіть "Man" або "Woman"')  # і програма знову запитає дані
            continue
        for k in template.keys():  # Перебираємо ключі у зразку, та додаємо до них значення від користувача
            if element == 1:
                template[k] = int(user_data[element])
            elif element == 3:
                template[k] = str(EyeColour(int(user_data[element])).name)
            else:
                template[k] = user_data[element]
            element += 1
        data_base.append(
            dict(template))  # Якщо зразок утвориться правильно, то він добавиться в загальний базу даних туристів
    except (ValueError,
            IndexError):  # якщо користувач введе дані невірно - йому виб'є помилку і знову запросить ввести дані
        print('Ви ввели не вірно дані!')
        element = 0

data_base.sort(key=lambda x: x['surname'])  # База данних туристів сортується за прізвищем

user_id = 1
for user in data_base:  # Виводиться на екран відсортований список туристів
    print(f"{user_id}. {user['surname']} {user['years']} {user['gender']} {user['eye']}")
    user_id += 1
print(
    f'\nСередньостатичний вік серед групи туристів: {averageAge(data_base)}\n'  # Виводиться середній вік усіх туристів,
    f'Чоловіки: {averageGender(data_base)[0]}%\n'                               # відсоток чоловіків,
    f'Жінки:    {averageGender(data_base)[1]}%')                                # та відсоток жінок
