from random import randint
g = randint(0,9)
p = randint(0,9)
b = randint(0,9) #Иммитация публичного ключа второго пользователя
a = int(input('Введите ваш публичный ключ: '))
def diffi_hellman_step1(a,g,p):
    A=g^a % p
    return(A)
A=diffi_hellman_step1(a,g,p)
print(A)
def diffi_hellman_step2(A,b,g,p):
    B=g^b % p
    K=A^b % p
    return(B)
B=diffi_hellman_step2(A,b,g,p)
def diffi_hellman_step3(B,a,p):
    KEY=B^a % p
    return(KEY)
KEY=diffi_hellman_step3(B,a,p)
print(KEY)