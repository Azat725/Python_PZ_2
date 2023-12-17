a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

user_choice = ('Введите операцию')

if user_choice == 'Сумма':
    sum = a + b + c
    print(sum)
elif user_choice == 'Произведение':
    pro = a * b * c
    print(pro)