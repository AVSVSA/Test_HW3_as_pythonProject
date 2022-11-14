
separator = input('Введите любой символ:')

sq_side = int(input('Введите длину стороны квадрата:'))
print ('Вывод:', f'Периметр: {sq_side * 4}',f'Площадь: {sq_side ** 2}', '', sep='\n' )

rect_length = int(input('Введите длину прямоугольника:'))
rect_width = int(input('Введите ширину прямоугольника:'))
print ('Вывод:', f'Периметр: {(rect_length + rect_width) * 2}',f'Площадь: {rect_length * rect_width}', '', sep='\n' )

print (f'{separator * (sq_side * 4 + rect_length * rect_width)}', '', sep='\n')

monthly_salary = int(input('Введите заработную плату в месяц:'))
mortgage_percent = int(input('Введите, какой процент(%) уходит на ипотеку:'))
cost_of_life_percent = int(input('Введите, какой процент(%) уходит на жизнь:'))

print ('Вывод:', f'На ипотеку было потрачено: {monthly_salary // 100 * mortgage_percent * 12} рублей' , f'Было накоплено: {(monthly_salary - monthly_salary//100*(mortgage_percent+cost_of_life_percent))*12} рублей', sep='\n')

