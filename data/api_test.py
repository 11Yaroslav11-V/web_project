from requests import get

# все записи
print(get('http://localhost:5000/api/order').json())
# запись 1
print(get('http://localhost:5000/api/order/1').json())
# несуществующая запись
print(get('http://localhost:5000/api/order/500').json())
# ошибочный запрос
print(get('http://localhost:5000/api/order/abc').json())
