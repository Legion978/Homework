#Задание 1
list = ["apple ", "cola ","milk","bread ","towel"]
for i in range (len(list)):
    print(list[i], '+')

Presidents_and_countries = {'Russia': 'Vladimir Putin', 'USA' : "John Baiden", 'Italia':'Sergio Mattarella'}
print('Президенты и страны:',Presidents_and_countries)

for key, value in Presidents_and_countries.items():
    print('Ключи и значения:',key,value)


#Задание 2

step = [3**x for x in range(2, 15, 3)]
print('Степени тройки в диапазоне от 2 до 15 с шагом 3:',step)


# Задание 3
i = 0
for i in range (2,20):
    if i >1:
        for n in range(2,i):
            if(i % n) == 0:
                break

        else:
            print('Простые числа:',i)






























