from requests import get, put
# изменяем статус заказа
# готово - игра опубликована
# в процессе - будет опубликована очень скоро
# отказ - нет прав на публикацию игры

# перед изменением стоит посмотреть все записи или запись в таблице
print(get('http://localhost:5000/api/order/3').json())

# Empty request
print(put('http://localhost:5000/api/order/3').json())

# изменить статус заказа
print(put('http://localhost:5000/api/order/1', json={'status': 'в процессе'}).json())
print(put('http://localhost:5000/api/order/3', json={'status': 'отказано'}).json())

# посмотреть результат изменения
print(get('http://localhost:5000/api/order/1').json())
print(get('http://localhost:5000/api/order/3').json())
