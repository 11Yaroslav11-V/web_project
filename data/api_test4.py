from requests import get, delete


# перед удалением стоит посмотреть имеющиеся записи в таблице
print(get('http://localhost:5000/api/order').json())

# ошибка - нет записи с номером 6998
print(delete('http://localhost:5000/api/order/6998').json())

# удалить существующую запись 3 и посмотреть результат
print(delete('http://localhost:5000/api/order/3').json())
print(get('http://localhost:5000/api/order').json())

