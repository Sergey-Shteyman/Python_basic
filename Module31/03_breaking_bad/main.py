import requests
import json

request = requests.get("https://www.breakingbadapi.com/api/deaths")
data = json.loads(request.text)
with open("breaking_bad.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent=4)

max_death = 0
for season in data:
    if season["number_of_deaths"] > max_death:
        max_death = season["number_of_deaths"]

for season in data:
    if max_death == season["number_of_deaths"]:
        print(f"ID эпизода: {season['death_id']}")
        print(f'Номер сезона: {season["season"]}')
        print(f'Номер эпизода: {season["episode"]}')
        print(f'Общее количество смертей: {season["number_of_deaths"]}')
        print(f'Список погибших: {season["death"]}')
