HELP = '''
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи
exit - завершить ввод задач
'''


tasks = {}
today, tomorrow, other = [], [], []

run = True


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
        # print(tasks, )
        # print('Сегодня: ', today, sep='\n')
        # print('Завтра: ', tomorrow, sep='\n')
        # print('В другие дни: ', other, sep='\n')
    elif command == 'add':
        task = input('Введите название задачи: ')
        date = input('Когда вы хотите выполнить данную задачу? (Сегодня/Завтра/Не знаю): ')
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = []
            tasks[date].append(task)
            print(f'Задача {task} добавлена на дату {date}')
        if date == 'Сегодня':
            today.append(task)
        elif date == 'Завтра':
            tomorrow.append(task)
        else:
            other.append(task)
        # print(f'Задача {task} добавлена!')
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Вы ввели неизвестную команду. Пожалуйста, введите существующую команду')
        print(HELP)
        run = True