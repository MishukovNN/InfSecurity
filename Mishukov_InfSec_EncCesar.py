alf1='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' #string английская библиотека
alf2='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #string русская библиотека
lang = input('Выберите язык (ru/en): ')   #Реализую ввод и на русском и на английском (заодно и проверю, работает ли русский язык без библиотеки    
if lang != 'en' and lang != 'ru': #Пользовательская ошибка
    print('Данные введены вами некорректно, попробуйте в следующий раз')
else:
    message = input("Введите вашу фамилию на выбранном языке: ").upper() #Ввод
    temp = int(input('Введите ваш публичный ключ: ')) #A
    itog = '' #string для вывода
    if lang == 'ru': #Русская фамилия
        for i in message:
            mesto = alf2.find(i)
            new_mesto = mesto + temp
            if i in alf2:
                itog += alf2[new_mesto]
            else:
                itog += i
        print (itog)
    else: #Английская фамилия
        for i in message:
            mesto = alf1.find(i)
            new_mesto = mesto + temp
            if i in alf1:
                itog += alf1[new_mesto]
            else:
                itog += i
        print (itog)