import re


auto_numbers = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"
private_car = re.findall(r"[а-яА-Я]\d{3}[а-яА-Я]{2}\d{2,3}", auto_numbers)
taxi_car = re.findall(r"[а-яА-Я]{2}\d{3}\d{2,3}", auto_numbers)

print(f"Список номеров частных автомобилей: {private_car}")
print(f"Список номеров такси: {taxi_car}")
