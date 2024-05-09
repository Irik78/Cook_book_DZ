with open('cook.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        name_dish = i.strip()
        quantity_ingred = int(file.readline())
        ingredients = []
        for x in range(quantity_ingred):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure':measure})
        cook_book[name_dish] = ingredients
        file.readline()
        print(cook_book)