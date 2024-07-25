alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where" said Alice.\n'
'"Then it doesn\'t matter which way you go," said the Cat.\n'
'"So long as I get somewhere," Alice added as an explanation.\n'
'"Oh, you\'re sure to do that," said the Cat,\n'
'"If you only walk long enough."')

for single_quote in alice_in_wonderland:
    if single_quote == "'":
        print(single_quote)

print(f"{alice_in_wonderland}")

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_sea_area = black_sea_area + azov_sea_area
print(f"Загальна площа Чорного та Азовського морыв разом: {total_sea_area}")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_product = 375291
first_storage_and_second_storage = 250449
second_storage_and_third_storage = 222950

third_storage = total_product - second_storage_and_third_storage
second_storage = second_storage_and_third_storage - third_storage
first_storage = first_storage_and_second_storage - second_storage

print(f"На першому складі розміщено {first_storage} товарів")
print(f"На другому складі розміщено {second_storage} товарів")
print(f"На третьому складі розміщено {third_storage} товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
one_month = 1179
eighteen_months = one_month * 18
computer_cost = eighteen_months
print(f"вартість комп’ютера {computer_cost}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019
result = a % 8
print(result)

b = 9907
result = b % 9
print(result)

c = 2789
result = c % 5
print(result)

d = 7248
result = d % 6
print(result)

e = 7128
result = e % 5
print(result)

f = 19224
result = f % 9
print(result)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_large = 4 * 274
pizza_middle = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21

total_price = pizza_large + pizza_middle + juice + cake + water
print(f"Іринці знадобиться {total_price} грн для даного замовлення")

pizza_large_price = 274
pizza_middle_price = 218
juice_price = 35
cake_price = 350
water_price = 21

pizza_large_quantity = 4
pizza_middle_quantity = 2
juice_quantity = 4
cake_quantity = 1
water_quantity = 3

total_price = (pizza_large_price * pizza_large_quantity + pizza_middle_price * pizza_middle_quantity + cake_price * cake_quantity + juice_price * juice_quantity + water_price * water_quantity)
print(f"Іринці знадобиться {total_price} грн для даного замовлення")
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo = 232
one_page = 8
total_pages = (total_photo / one_page)
print(f"{total_pages} сторінок знадобиться Ігорю, щоб вклеїти всі фото")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?R
"""
distance = 1600
fuel_100_km = 9
tank_capacity = 48

total_fuel = (distance / 100) * fuel_100_km
print(f"{total_fuel} літрів бензину знадобиться для такої подорожі")

total_tanks_nubmer = total_fuel / tank_capacity
visits_refueling_stations = total_tanks_nubmer
print(f"{visits_refueling_stations} разів родині необхідно заїхати на заправку під час цієї подорожі")
