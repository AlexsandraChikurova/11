def rest():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт")

    newRestaurant = Restaurant("Pug", "Грузинская")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
def rests3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт")

    restaurant1 = Restaurant("Pug 1", "Французская")
    restaurant2 = Restaurant("Pug 2", "Азиатская")
    restaurant3 = Restaurant("Pug 3", "Вьетнамская")

    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()

    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()

    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()

def restsR():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт")

        def up_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")

    restaurant1 = Restaurant("Pug 1", "Французская", 3)

    restaurant1.describe_restaurant()
    restaurant1.up_rating(5)
    restaurant1.describe_restaurant()
while True:
    print('1. ресторан')
    print('2. 3 ресторана')
    print('3. рейтинг')
    print('4. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        rest()
    elif a == 2:
        rests3()
    elif a == 3:
        restsR()
    elif a == 4:
        break
    else:
        print('Неверное действие')