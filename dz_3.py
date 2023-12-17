metre = int(input('Введите количество метров: '))

user_choice = ('Введите операцию')

if user_choice == 'Дюймы':
    inc = metre//39.37
    print(inc + 'дюймов')
elif user_choice == 'Мили':
    miles = metre * 0.00062
    print(miles + 'миль')
elif user_choice == 'Ярды':
    yard = metre * 0.914
    print(yard + 'ярдов')