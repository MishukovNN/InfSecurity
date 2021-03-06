alf1='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' #string английская библиотека
alf2='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #string русская библиотека
lang = input('Выберите язык (ru/en): ')   #Реализую ввод и на русском и на английском (заодно и проверю, работает ли русский язык без библиотеки    
if lang != 'en' and lang != 'ru': #Пользовательская ошибка
    print('Данные введены вами некорректно, попробуйте в следующий раз')
else:
    message = input("Введите вашу фамилию на выбранном языке: ").upper() #Ввод
    a = int(input('Введите ваш публичный ключ: ')) #a в алгоритме Диффи Хеллмана
    itog = '' #string для вывода
    new_itog = '' #string для дешифровки
    from random import randint
    g = randint(0,9)
    p = randint(0,9)
    b = randint(0,9) #Иммитация публичного ключа второго пользователя
    def diffi_hellman_step1(a,g,p):
        A=g^a % p
        return(A)
    A=diffi_hellman_step1(a,g,p)
    def diffi_hellman_step2(A,b,g,p):
        B=g^b % p
        K=A^b % p
        return(B)
    B=diffi_hellman_step2(A,b,g,p)
    def diffi_hellman_step3(B,a,p):
        KEY=B^a % p
        return(KEY)
    KEY=diffi_hellman_step3(B,a,p)
    if lang == 'ru': #Русская фамилия
        for i in message:
            mesto = alf2.find(i)
            new_mesto = mesto + KEY
            if i in alf2:
                itog += alf2[new_mesto] #Заполнение итога
            else:
                itog += i
        print ('Ваша фамилия зашифрована: ',itog)
    else: #Английская фамилия
        for i in message:
            mesto = alf1.find(i)
            new_mesto = mesto + KEY
            if i in alf1:
                itog += alf1[new_mesto] #Заполнение итога
            else:
                itog += i
        print ('Ваша фамилия зашифрована: ',itog)
    print ('Ваш приватный ключ: ',KEY) #С точки зрения инф. безопасности нельзя показывать pkey, однако у нас пример работы)
    #Т.е. можно просто стереть 46 строчку (предыдущую) и никто pkey не узнает))
    name_dec_otv = input('Хотите расшифровать вашу фамилию (y/n): ')  #Пользователь может отказаться от расшифровки
    if name_dec_otv == 'y':
        if lang == 'ru': #Русская фамилия для дешифровки
            for i in itog:
                mesto1 = alf2.find(i)
                new_mesto1 = mesto1 - KEY
                if i in alf2:
                    new_itog += alf2[new_mesto1] #Заполнение итога
                else:
                    new_itog += i
            print ('Ваша фамилия расшифрована: ',new_itog)
        else: #Английская фамилия
            for i in itog:
                mesto1 = alf1.find(i)
                new_mesto1 = mesto1 - KEY
                if i in alf1:
                    new_itog += alf1[new_mesto1] #Заполнение итога
                else:
                    new_itog += i
            print ('Ваша фамилия расшифрована: ',new_itog)
    else:
        print ('Работа шифровальщика закончена, всего хорошего!')