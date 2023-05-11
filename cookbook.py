from pprint import pprint
with open('text.txt', encoding='utf-8') as open_file, open ('cookbook.txt', 'w', encoding='utf-8') as open_file2:
    cook_book = {} 
    for line in open_file:
        dish_name = line.strip()
        ingredients_count = int(open_file.readline())
        list_ingredient = []
        for _ in range(ingredients_count):
            ing = open_file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            my_dict = {'ingredient_name' : ingredient_name,'quantity' : quantity,'measure' : measure}
            list_ingredient.append(my_dict)
            cook_book[dish_name] = list_ingredient
        open_file.readline()
pprint(cook_book, indent=2)    

#------------------------------- ФУНКЦИЯ-------------------------------------------------

person_count = 2
dishes = ['Фахитос', 'Омлет']
ingredient_quantity_measure = {}
def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        list_ingr = cook_book[dish]
        for ingr in  list_ingr:  
            ingredient_name, quantity, measure = ingr.values()          
            quantity = str(int(quantity) * person_count)
            if not ingredient_name in ingredient_quantity_measure:
                ingredient_quantity_measure[ingredient_name] = {'quantity': quantity, 'measure' : measure.strip()}
            else:
                x = int(ingredient_quantity_measure[ingredient_name]['quantity'])
                ingredient_quantity_measure[ingredient_name]['quantity'] = str(x + int(quantity))
    pprint(ingredient_quantity_measure)
    print()

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)  

# Задача №3

with open('t1.txt', encoding='utf-8') as file1, open('t2.txt', encoding='utf-8') as file2, open('t3.txt', encoding='utf-8') as file3, open('new_file.txt','w', encoding='utf-8') as new_file:        
    def sort_list(main_list):
        return main_list[1]
    
    list_files = [file1, file2, file3]
    main_list = []
    list_write = []
    for file in list_files:
        lines = file.readlines()
        lines[-1] = lines[-1] + '\n'
        list_write.append(file.name + '\n')
        list_write.append(str(len(lines)) + '\n')
        list_write += lines
        main_list.append(list_write)
        list_write = []
    main_list.sort(key=sort_list)
    write_list = [''.join(i) for i in main_list]
    new_file.writelines(write_list)