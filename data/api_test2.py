from requests import get, post

# empty request (пустой)
print(post('http://localhost:5000/api/order').json())

# неполный  Bad request
print(post('http://localhost:5000/api/order', json={'company': '4A GAMES'}).json())

# верный
# print(post('http://localhost:5000/api/order', json={'company': '4A GAMES', 'game_name': 'Metro 2033',
#                                                    'status': 'заказ'}).json())
# print(post('http://localhost:5000/api/order', json={'company': 'UBISOFT', 'game_name': 'Far cry 5',
#                                                    'status': 'заказ'}).json())
# print(post('http://localhost:5000/api/order', json={'company': 'Valve', 'game_name': 'Half-life',
#                                                    'status': 'заказ'}).json())
print(post('http://localhost:5000/api/order', json={'company': '4A GAMES', 'game_name': 'Metro Redux',
                                                    'status': 'заказ'}).json())
print(get('http://localhost:5000/api/order').json())
