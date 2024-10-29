# TODO Напишите функцию для поиска индекса товара
def poisktovara(list, tovar):
    if tovar in list:
        return list.index(tovar)  # Возвращаем индекс элемента
    else:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = poisktovara(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
