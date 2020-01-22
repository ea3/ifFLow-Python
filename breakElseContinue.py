# shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
# for item in shopping_list:
#     if item == 'spam':
#         continue
#         #break
#     print('Buy ' + item)

meal = ['egg', 'bacon', 'bean', 'sausages']
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        # break
else:                               # ELSE  IS HERE INDENTED FOR THE "FOR"
    print("I will have a plate of that, the, please")

if nasty_food_item:
    print("Can't have anything without spam in it")
