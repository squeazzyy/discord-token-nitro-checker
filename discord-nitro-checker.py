import requests

with open('tokens.txt') as f:
    tokens = [line.strip() for line in f]

headers = {
    'Content-Type': 'application/json'
}

for token in tokens:
    headers['Authorization'] = token
    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        has_nitro = user_data.get('premium_type', 0) > 0
        print(f"Токен {token} соответствует пользователю {user_data['username']} ({'есть' if has_nitro else 'нету'} Nitro)")
    else:
        print(f"Ошибка при запросе информации о пользователе с токеном {token}: {response.status_code} {response.reason}")
