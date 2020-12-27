import database

item_list = []
price_list = []
while True:
    try:
        items = input(
            'Enter the item you have purchased("exit" to Exit): ').lower()
        if items == 'exit':
            break
        item_list.append(items)
        prices = int(input('Enter the price of the item: $'))
        price_list.append(prices)
    except ValueError:
        print('check the entered values properly!')

index = 0
total_fruit_price = 0
total_vege_price = 0
for item in item_list:
    if item in database.FRUITS:
        # Finds the corresponding price of the fruit
        index = item_list.index(item)
        # Finds the toal price of the fruits purchased
        total_fruit_price += price_list[index]
    elif item in database.VEGES:
        # Finds the corresponding price of the vegetable
        index = item_list.index(item)
        # Finds the toal price of the vegetables purchased
        total_vege_price += price_list[index]


print('*Total expenses*')
print(f'FRUITS: ${total_fruit_price}\nVEGES:  ${total_vege_price}\nTOTAL:  ${total_fruit_price + total_vege_price}')
