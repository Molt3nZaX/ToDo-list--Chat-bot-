import random

HELP = '''
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи
exit - завершить ввод задач
random - случайная задача на сегодня
'''


tasks = {}
# today, tomorrow, other = [], [], []


random_tasks = ['"Погулять"', '"Велопрогулка"', '"Почитать любимую книгу"', '"Го на скалодром"']
run = True  # триггер для цикла while

def add_todo(date, task):
    if date in tasks:  # Если дата есть в словаре, то добавляем задачу в список
        tasks[date].append(task)
    else:  # Если даты нет в словаре, то создаем запись с ключом date
        tasks[date] = []
        tasks[date].append(task)
    print(f'Задача: {task} добавлена на дату: {date}')


print('Приветствую! Я - бот, который поможет Вам спланировать повседневные задачи. Чтобы ознакомиться со списком комманд - введите "help"')

while run:
    command = input('Введите команду (help, add, show): ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(tasks, )
        date = input('Введите дату для отображения списка задач: ')
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print('Такой даты нет')

    elif command == 'add':
        task = input('Введите название задачи: ')
        date = input('Введите дату выполнения задачи: ')
        add_todo(date, task)

    elif command == 'random':
        task = random.choice(random_tasks)
        add_todo('Сегодня', task)

    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Вы ввели неизвестную команду. Пожалуйста, введите существующую команду')
        print(HELP)
        run = True