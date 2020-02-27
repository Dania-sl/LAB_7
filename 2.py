'''
Задача. Визначити наймолодшого працівника і надрукувати відомості про нього.
Поля структури: Прізвище, Рік народження, Посада, Зарплатня, Освіта.
'''
while True:
    while True:
        try:
            count_of_worker = int(input('Count of worker: '))
            break
        except ValueError:
            print('Enter correct value')
    person_list = []
    person_dict = {}
    for i in range(1, count_of_worker + 1):
        while True:
            try:
                surname = input('Enter worker`s surname: ')
                year_of_born = int(input('Enter year of born: '))
                position = input('Enter position of worker: ')
                salary = int(input('Salary of worker: '))
                education = input('Worker`s education: ')
                person_dict[f'surname'] = surname
                person_dict[f'year of born'] = year_of_born
                person_dict[f'position'] = position
                person_dict[f'salary'] = salary
                person_dict[f'education'] = education
                person_list.append(person_dict)
                person_dict = {}
                break
            except ValueError or KeyError:
                print('Enter correct value')
    year = 0
    element = 0
    for person in range(0, len(person_list)):
        person_year = person_list[person].get('year of born')
        if year < person_year:
            year = person_year
            final_person = person
    print(person_list[final_person])
    if input('Press Enter if you want continue:') != '':
        break
