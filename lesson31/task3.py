import requests

API_TOKEN = 'ff631e58cb7eb39cf2a22232f33daf07'

city = input('Enter city: ').capitalize()

params = {
    'q': city,
    'appid': API_TOKEN,
    'units': 'metric',
    'lang': 'ua',
}

resp = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
if resp.ok:
    json_resp = resp.json()

    print(f'Погода в місті {city}: \n'
          f'{json_resp['main']['temp']} градус(ів) цельсію, '
          f'{json_resp['weather'][0]['main']}')

else:
    raise NameError(f'Немає міста з назвою <{city}>!!!')

