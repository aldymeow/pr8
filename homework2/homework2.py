while True:
    print('Введите целые числа: ')
    a = input()
    b = input()
    if isinstance(a, int)==1 and isinstance(b, int)==1:
        c = a + b
        print (f"Их сумма = {c}")
    else: 
        print ("Введенные вами данные не соответствуют условию")
        break