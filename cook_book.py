def get_cook_book(file_path: str) -> dict:
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        recipe = []
        dish_name = None
        ingredients_count = None
        for line in file:
            line = line.strip()
            if not line:
                continue
            if not dish_name:
                dish_name = line
            elif not ingredients_count:
                ingredients_count = int(line)
            else:
                ingredient_name, quantity, measure = line.split('|')
                recipe.append({
                    'ingredient_name': ingredient_name.strip(),
                    'quantity': int(quantity.strip()),
                    'measure': measure.strip()
                })
                ingredients_count -= 1
                if ingredients_count == 0:
                    cook_book[dish_name] = recipe
                    dish_name = None
                    ingredients_count = None
                    recipe = []
    return cook_book


cook_book = get_cook_book('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
    return shop_list


# Пример использования функции
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)