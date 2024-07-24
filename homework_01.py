

# task 01 == Виправте синтаксичні помилки

print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f"Периметр = {perimetery}")

# task 07

"""У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?"""

apples = 4
pear = apples + 5
plum = apples - 2

Summ_trees = apples + pear + plum
print(f"Summ trees in the garden = {Summ_trees}")

# task 08

"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

temperature_morning = 5
temperature_afternoon = temperature_morning - 10
temperature_evening = temperature_afternoon + 4

print(f"Temperature in the evening = {temperature_evening}")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys / 2
sick_boy = 1
absent_girls = 2

total_children = boys + girls - sick_boy - absent_girls
print (f"Toda is {total_children}")
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book1_price = 8
book2_price = book1_price + 2
book3_price = (book1_price + book2_price) / 2

total_cost = book1_price + book2_price + book3_price

print(f"Summ of the books {total_cost}")


# """
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
# """
# book1_price = 8
# book2_price = book1_price + 2
# book3_price = (book1_price + book2_price) / 2
#
# total_cost = book1_price + book2_price + book3_price
#
# print(f"Summ of the books {total_cost}")